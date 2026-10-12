#variables
temperature=0.7 #float
max_tokens=1024 #int
is_streaming=False #boolean
content_box=None #None

# Type Hints
model_name:str="gemini-2.0-flash"
temperature:float=0.7 #float
max_tokens:int=1024 #int
is_streaming:bool=False #boolean
content_box:str|None=None #None
print(type(model_name))

#Strings:immutable | string formatting
name="LLM"
score=97.3
#Old version
print("Hello %s"%name)
print("Score %.1f"%score)

#f-strings(py 3.6+)
print(f"Hello {name}")
print(f"Score: {score:.1f}")

#expressions inside f-strings
word_limit=200
print(f"{'Over' if word_limit>150 else 'under'}limit")
data={"topic":"RAG"}
print(f"Topic: {data['topic']}")

#Format specifiers
pi=3.14159265
print(f"pi:{pi:.2f}")

#debugging =
temp=0.7
print(f"{temp=}")

#Multi line f-strings formatting
user_input="what is Langchain?"
context_text="Langchain is a framework for building LLM apps"
system_prompt=f"""
you are a helpful AI tutor.
context provided:{context_text} 
student question:{user_input} 
instructions:
-Answer based only on the context above 
-If the answer is not in the context,say "I don't know" 
-keep your answers under 3 sentences
""".strip()
print(system_prompt)

#Lists: ordered,mutable,heterogenous sequences
#in gen ai:chat history,chunks of retreived documents
#token sequences
chat_history:list[dict]=[
    {"role":"user","content":"what is an LLM"},
    {"role":"assistant","content":"A LLM is a neural n/w trained on vast amounts of text."},
]
#Access
first_msg=chat_history[0]
print(first_msg)
print(chat_history[-1]["content"]) #last element

#modify
chat_history.append({"role":"user","content":"what is a RAG?"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

#Iterate
for msg in chat_history:
    print(f"{msg['role'].upper()}:{msg['content']}")

#list of document chunks
chunks:list[str]=[
    "RAG stands for retreival Augmented generation",
    "it combines a retreiver with a generator"
]
#filter chunks based on length
valid_chunks=[c for c in chunks if len(c.split())>=6]
print(valid_chunks)