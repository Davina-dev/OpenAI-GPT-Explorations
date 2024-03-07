import os
from openai import OpenAI
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Inicializa el cliente de OpenAI
client = OpenAI()

# Define el modelo por defecto
model_default = "gpt-3.5-turbo"

def analyze_feelings(text, model=model_default):
    # Crea el prompt con el texto a analizar
    prompt = f"Por favor, analiza el sentimiento predominante en el siguiente texto: '{text}'. El sentimiento es: "
    
    # Llama a la API de OpenAI para analizar el sentimiento
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.5
    )
    return response.choices[0].message.content

# Solicita al usuario que ingrese un texto para analizar
texto_para_analizar = input("🤖 ingresa un texto sin saltos de linea: ")
sentimiento = analyze_feelings(texto_para_analizar)

# Imprime el sentimiento analizado corrigiendo el error de typo en la variable 'sentimiento'
print(f"🤖 Sentimiento analizado: {sentimiento}")