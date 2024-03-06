import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables for accessing the OpenAI API
load_dotenv()
client = OpenAI()
print("API Key:", client.api_key)

# Here we make a call to the OpenAI API to generate a humorous story about being a junior developer
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
 messages=[
    {"role": "system", "content": "You are a comedic assistant, gifted in unraveling the mysteries of coding with humor and wit."},
    {"role": "user", "content": "Craft a humorous anecdote that captures the essence of being a junior developer eager to learn."}
]
)
print(completion.choices[0].message.content)
