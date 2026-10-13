#first API Call to ollama
from openai import OpenAI
client=OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")
r=client.chat.completions.create(model="phi3:mini",messages=[{"role":"user","content":"what is an LLM?answer in 3 sentences"}],)
print(r.choices[0].message.content)
print(f"Tokens used:{r.usage.total_tokens}")
