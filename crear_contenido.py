import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()

def crear_contenido(article_topic, num_words, creativity_level, model="gpt-3.5-turbo"):
    prompt = f"Por favor, escribe un artículo corto sobre un tema: {article_topic}\n\n"
    response= client.chat.completions.create(
        model= model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens= num_words,
        temperature= creativity_level
    )
    return response.choices[0].message.content

def resumir_texto(text, num_words, ceativity_level,model="gpt-3.5-turbo"):
    prompt = f"Por favor, resume el siguiente texto: {text}\n\n"
    respuesta= client.chat.completions.create(
            model= model,
            messages= prompt,
            n= 1,
            max_tokens= num_words,
            temperature= ceativity_level
        )
    return respuesta.choices[0].message.content

article_topic= input('🤖:Elige un tema para tu artículo: ')
num_words=  int(input('🤖:¿Cuántas palabras quieres que tenga tu artículo? '))
ceativity_level= int(input('🤖:¿Del 1 al 10, que tan creativo quieres que sea tu artículo? '))/10

articulo_creado = crear_contenido(article_topic, num_words, ceativity_level)
print(articulo_creado)