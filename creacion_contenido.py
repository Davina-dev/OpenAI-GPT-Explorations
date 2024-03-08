import os
from openai import OpenAI
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Inicializa el cliente de OpenAI
client = OpenAI()

model_default = "gpt-3.5-turbo"

def generate_prompt(article_topic=None, original_article=None, is_article=True):
    """Construye un prompt para solicitar la generación de contenido."""
    if is_article:
        return f"Por favor, escribe un artículo corto sobre el tema: {article_topic}"
    else:
        return f"Por favor, resume el siguiente texto: {original_article}"

def generate_content(prompt, tokens=300, creativity_level=0.7, model=model_default):
    """Genera contenido basado en un prompt, utilizando la API de OpenAI."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=tokens,
        temperature=creativity_level
    )
    return response.choices[0].message.content

def main():
    opcion_usuario = input('🤖: ¿Quieres escribir un artículo (1) o hacer un resumen (2)? Ingresa 1 o 2: ')

    if opcion_usuario not in ['1', '2']:
        print('Opción no reconocida. Por favor, inicia el programa de nuevo y selecciona 1 o 2.')
        return

    tokens = int(input('🤖: ¿Cuántos tokens quieres que tenga el contenido? '))
    creativity_level = float(input('🤖: ¿Del 1 al 10, qué tan creativo quieres que sea? ')) / 10

    if opcion_usuario == '1':
        article_topic = input('\n Elige un tema para tu artículo: ')
        prompt = generate_prompt(article_topic=article_topic, is_article=True)
    else:
        original_article = input('\n Pega el artículo que quieras resumir, sin saltos de línea: ')

        prompt = generate_prompt(original_article=original_article, is_article=False)

    content = generate_content(prompt, tokens, creativity_level)
    print(f"\n 👉: {content}")

if __name__ == "__main__":
    main()