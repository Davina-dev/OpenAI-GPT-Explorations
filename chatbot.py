import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the OpenAI client using the API key loaded from the .env file
client = OpenAI()

# Lists to store the history of questions and answers
preguntas_anteriores = []
respuestas_anteriores = []


# Function to ask a question to ChatGPT
def preguntar_chat_gpt(prompt, model="gpt-3.5-turbo"):
    # Make a request to the OpenAI API to get a response for the prompt
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message.content

# Greet the user
print("Bienvenido a mi chatbot de prueba. Escribe 'salir' cuando quieras terminar")

# Main loop for the chat
while True:
    # Initialize the historical conversation string
    conversacion_historica = ""
    
    # Get user input
    ingreso_usuario = input("\n🤓 Tú: ")
    
    # Check if the user wants to exit
    if ingreso_usuario.lower() == "salir":
        break

    # Build the historical conversation string
    for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion_historica += f"El usuario pregunta: {pregunta}\n"
        conversacion_historica += f"ChatGPT responde: {respuesta}\n"

    # Get the response from ChatGPT for the current prompt
    prompt = preguntar_chat_gpt(ingreso_usuario)
    conversacion_historica += prompt
    respuesta_gpt = preguntar_chat_gpt(conversacion_historica)
    
    # Print ChatGPT's response
    print(f"🤖: {respuesta_gpt}")

    # Update the history lists
    preguntas_anteriores.append(ingreso_usuario)
    respuestas_anteriores.append(respuesta_gpt)