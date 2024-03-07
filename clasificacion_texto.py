import os
from openai import OpenAI
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Inicializa el cliente de OpenAI
client = OpenAI()

def clasificar_texto(text):
   categorias = [
      "Tecnología", 
      "Moda",
      "Alimentación",
      "Deportes", 
      "Viajes", 
      "Educación", 
      "Salud y Bienestar", 
      "Entretenimiento", 
      "Hogar y Jardín", 
      "Arte y Cultura"
    ]
   prompt = f"Por favor, clasifica el siguiente texto '{text}' en una de estas categotias: {','.join(categorias)}. La categoria es: "
   response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50,
        temperature=0.5
    )
   return response.choices[0].message.content

texto_para_clasificar = input("🤖: Ingresa un texto para clasificar: ")
clasificacion = clasificar_texto(texto_para_clasificar)
print(f"🤖 Categoría del texto: : {clasificacion}")