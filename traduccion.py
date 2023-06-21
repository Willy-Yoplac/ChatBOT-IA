import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def traducir(texto, idioma):
    prompt = f"Traduce el texto '{texto}' al {idioma}\n\n"
    respuesta = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        n=1,
        temperature = 0.5,
        max_tokens = 100
        
    )
    return respuesta.choices[0].text.strip()

mi_texto = input("Escribe el texto que quieres traducir: ")
mi_idioma = input("A que idioma lo quieres traducir: ")
traducion = traducir(mi_texto,mi_idioma)
print(traducion)