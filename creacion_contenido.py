import os
from openai import OpenAI
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Inicializa el cliente de OpenAI
client = OpenAI()

model_default = "gpt-3.5-turbo"

def create_prompt_for_article(article_topic):
    """Construye un prompt para solicitar la generación de un artículo."""
    return f"Por favor, escribe un artículo corto sobre el tema: {article_topic}"

def create_prompt_for_summary(original_article):
    """Construye un prompt para solicitar el resumen de un texto."""
    return f"Por favor, resume el siguiente texto: {original_article}"

def generate_content(prompt, tokens, creativity_level, model=model_default):
    """Genera contenido basado en un prompt, utilizando la API de OpenAI."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=tokens,
        temperature=creativity_level
    )
    return response.choices[0].message.content

def crear_contenido(article_topic, tokens, creativity_level):
    prompt = create_prompt_for_article(article_topic)
    return generate_content(prompt, tokens, creativity_level)

def resumir_texto(original_article, tokens, creativity_level):
    prompt = create_prompt_for_summary(original_article)
    return generate_content(prompt, tokens, creativity_level)


# Solicita al usuario que elija entre escribir un artículo o hacer un resumen
opcion_usuario = input('🤖: ¿Quieres escribir un artículo (1) o hacer un resumen (2)? Ingresa 1 o 2: ')
print(opcion_usuario)

if opcion_usuario == '1':
    # Solicita al usuario que ingrese datos para generar un artículo
    article_topic = input('🤖: Elige un tema para tu artículo: ')
    tokens = int(input('🤖: ¿Cuántos tokens quieres que tenga tu artículo? '))
    creativity_level = float(input('🤖: ¿Del 1 al 10, qué tan creativo quieres que sea tu artículo? ')) / 10
    articulo_creado = crear_contenido(article_topic, tokens, creativity_level)
    print(articulo_creado)
elif opcion_usuario == '2':
    # Solicita al usuario que ingrese el artículo a resumir
    original_article = input('🤖:Pega el artículo, sin saltos de línea, que quieras resumir: ')
    tokens = int(input('🤖:¿Cuántos tokens quieres que tenga tu resumen? '))
    creativity_level = float(input('🤖:¿Del 1 al 10, que tan creativo quieres que sea el resumen? '))/10
    resumen = resumir_texto(original_article, tokens, creativity_level)
    print(resumen)
else:
    print('Opción no reconocida. Por favor, inicia el programa de nuevo y selecciona 1 o 2.')


