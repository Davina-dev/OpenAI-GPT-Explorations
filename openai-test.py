import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno y verificar que funciona
load_dotenv()
client = OpenAI()
print("API Key after:", client.api_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
 messages=[
    {"role": "system", "content": "You are a comedic assistant, gifted in unraveling the mysteries of coding with humor and wit."},
    {"role": "user", "content": "Craft a humorous anecdote that captures the essence of being a junior developer eager to learn."}
]
)
print(completion.choices[0].message.content)
