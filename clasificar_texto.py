import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def clasificar_texto(texto):
    categorias = [
        'arte',
        'ciencia',
        'deportes',
        'economía',
        'educacion',
        'entretenimiento',
        'medio ambiente',
        'politica',
        'salud',
        'tecnologia'
    ]

    prompt = f"\nPor favor clasifica el siguiente texto: '{texto}'. En una de estas categorias: {','.join(categorias)}. \n\n la categoria es: "
    respuesta = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        n=1,
        max_tokens = 50,
        temperature = 0.5
    )
    return respuesta.choices[0].text.strip()

# Hacemos el pedido
texto_para_clasificar = input("Ingresa un texto: ")
clasificacion = clasificar_texto(texto_para_clasificar)
print("\nClasificacion: ", clasificacion)
