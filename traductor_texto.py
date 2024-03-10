import os
from openai import OpenAI
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Inicializa el cliente de OpenAI con la clave de API desde las variables de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def traducir_texto(texto, idioma):
    prompt = f"Traduce el texto '{texto}' al idioma {idioma}."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content

def main():
    """
    Función principal que solicita al usuario un texto y un idioma, y muestra el texto traducido.
    """
    mi_texto = input("Texto: \n📃 - ")
    mi_idioma = input("Idioma: \n🌏 - ")
    try:
        traduccion = traducir_texto(mi_texto, mi_idioma)
        print(traduccion)
    except Exception as e:
        # Mejor manejo de errores para informar al usuario
        print(f"Error al traducir el texto: {e}")

if __name__ == "__main__":
    main()