import os
from openai import OpenAI
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Inicializa el cliente de OpenAI
client = OpenAI()


def traducir_texto(texto, idioma):
    prompt = ""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content
