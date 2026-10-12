#Functions:
def build_prompt(topic:str,word_limit:int=150)->str:
    return f"write about {topic}, with atmost {word_limit} words"
print(build_prompt("Gen AI"))
print(build_prompt("prompt Engg",word_limit=300))

# Brushes
# *args,**kwargs
# list comprehension,dict comprehension