import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

#funcion que va analizar el sentimiento
def analizar_sentimiento(texto):
    prompt = f"Por favor, analizar el siguiente texto: '{texto}'. \n\nEl sentiemiento es: "
    respuesta = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        n=1,
        max_tokens = 100,
        temperature = 0.5
    )
    return respuesta.choices[0].text.strip()

# Hacemos el pedido
texto_para_analizar = input("Ingresa un texto: ")
sentimiento = analizar_sentimiento(texto_para_analizar)
print("\n", sentimiento)