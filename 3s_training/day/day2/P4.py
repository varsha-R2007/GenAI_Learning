#First API call wrt Gemini
import google.generativeai as genai
import os
from dotenv import load_dotenv

#load the API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#create a model instance with config
#2.0,2.5,3.5
model=genai.GenerativeModel(model_name="gemini-3.8-flash",
                            generation_config={"temperature":0.7,"max_output_tokens":150},
                            system_instruction="You are a concise AI tutor.answer in 2-3 sentences.",)

#call the model
result=model.generate_content("what is a vector database?")
print(result.text)
print(f"Tokens:{result.usage_metadata.total_token_count}")
