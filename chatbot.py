import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the OpenAI client using the API key loaded from the .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Lists to store the history of questions and answers
preguntas_anteriores = []
respuestas_anteriores = []

def construir_contexto():
    """Construye el contexto de las conversaciones anteriores."""
    contexto = ""
    for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        contexto += f"El usuario pregunta: {pregunta}\nChatGPT responde: {respuesta}\n"
    return contexto

def preguntar_chat_gpt(prompt, model="gpt-3.5-turbo"):
    """Realiza una pregunta a ChatGPT y devuelve la respuesta."""
    contexto = construir_contexto()
    prompt_completo = contexto + "El usuario pregunta: " + prompt + "\nChatGPT responde:"
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt_completo}
        ],
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message.content

print("👋 Bienvenido a mi chatbot de prueba. Escribe 'salir' cuando quieras terminar.")

while True:
    ingreso_usuario = input("\n🤓 Tú: ")
    
    if ingreso_usuario.lower() == "salir":
        break

    respuesta_gpt = preguntar_chat_gpt(ingreso_usuario)
    
    print(f"🤖: {respuesta_gpt}")

    preguntas_anteriores.append(ingreso_usuario)
    respuestas_anteriores.append(respuesta_gpt)