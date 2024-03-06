import os
import openai
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar la clave API de OpenAI
client = openai.OpenAI()


def preguntar_chat_gpt(ingreso_usuario, model="gpt-3.5-turbo"):

    response = client.chat.completions.create (
        model=model,
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": ingreso_usuario}
    ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message.content

print("Bienvenido a mi chatbot de prueba. Escribe 'salir' cuando quieras terminar")

while True:
    ingreso_usuario = input("\n🤓 Tú: ")
    if ingreso_usuario.lower() == "salir":
        break

    respuesta_gpt = preguntar_chat_gpt(ingreso_usuario)
    print(f"🤖 Chatbot: {respuesta_gpt}")
