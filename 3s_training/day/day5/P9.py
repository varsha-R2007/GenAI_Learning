"""
P9.py - Mini-challenge: Build and query your own RAG (college document)

Pipeline: Load PDF -> Chunk -> Embed (Gemini) -> Store (ChromaDB) -> Retrieve -> Generate

PREREQUISITES:
- GEMINI_API_KEY in a local .env file
- pip install google-genai langchain-community langchain-text-splitters chromadb pypdf python-dotenv
"""

import os
from dotenv import load_dotenv
from google import genai
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ---- CHANGE THIS to your college document ----
PDF_PATH = r"C:\Users\varsh\Downloads\college_doc.pdf"

EMBED_MODEL = "gemini-embedding-001"
LLM_MODEL = "gemini-2.5-flash"

if not os.path.exists(PDF_PATH):
    raise SystemExit(f"File not found: {PDF_PATH!r}. Update PDF_PATH.")

# Step 1: load the PDF
pages = PyPDFLoader(PDF_PATH).load()
print(f"Pages loaded: {len(pages)}")

# Step 2: chunk
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
chunks = splitter.split_documents(pages)
texts = [c.page_content for c in chunks if c.page_content.strip()]
metas = [{"page": c.metadata.get("page", 0)} for c in chunks if c.page_content.strip()]
print(f"Chunks created: {len(texts)}")

# Step 3: embed (in batches of 100, the API limit per request)
embeddings = []
for i in range(0, len(texts), 100):
    batch = texts[i:i + 100]
    res = client.models.embed_content(model=EMBED_MODEL, contents=batch)
    embeddings.extend(e.values for e in res.embeddings)
print(f"Embeddings: {len(embeddings)} x {len(embeddings[0])} dims")

# Step 4: store in ChromaDB
db_client = chromadb.Client()
collection = db_client.create_collection("college_doc")
collection.add(
    documents=texts,
    embeddings=embeddings,
    metadatas=metas,
    ids=[f"chunk_{i}" for i in range(len(texts))],
)
print(f"Stored {collection.count()} chunks")

# Step 5: retrieve
def retrieve(question: str, top_k: int = 4):
    q_vec = client.models.embed_content(
        model=EMBED_MODEL, contents=[question]
    ).embeddings[0].values
    r = collection.query(query_embeddings=[q_vec], n_results=top_k)
    return r["documents"][0], r["metadatas"][0], r["distances"][0]

# Step 6: generate an answer from the retrieved chunks
def ask(question: str) -> str:
    docs, metas_, dists = retrieve(question)
    context = "\n\n".join(
        f"[Page {m['page'] + 1}] {d}" for d, m in zip(docs, metas_)
    )
    prompt = (
        "You are a helpful assistant for a college. Answer the question "
        "using ONLY the context below. If the answer is not in the context, "
        "say you couldn't find it in the document.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}"
    )
    resp = client.models.generate_content(model=LLM_MODEL, contents=prompt)
    pages_used = sorted({m["page"] + 1 for m in metas_})
    return f"{resp.text}\n\n(Sources: pages {pages_used})"

# Step 7: chat loop
print("\nRAG ready! Ask about your college document (type 'quit' to exit).")
while True:
    q = input("\nYou: ").strip()
    if q.lower() in ("quit", "exit"):
        break
    if q:
        print("\nAnswer:", ask(q))
