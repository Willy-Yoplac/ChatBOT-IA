import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def contenido (tema, tokens, temperatura, modelo = "text-davinci-002"):
    
    prompt = f"Por favor escribe un articulo corto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine = modelo,
        prompt = prompt,
        n=1,
        max_tokens = tokens,
        temperature = temperatura
    )
    return respuesta.choices[0].text.strip()

def resumir (texto, tokens, temperatura, modelo = "text-davinci-002"):
    prompt = f"Por favor resume el siguiente texto: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine = modelo,
        prompt = prompt,
        n=1,
        max_tokens = tokens,
        temperature = temperatura
    )
    return respuesta.choices[0].text.strip()

#============PARA CREAR UN ARTICULO O DOCUMENTO=============
#tema = input("Elige un tema para tu artículo: ")
#tokens = int(input("Cuántos tokens máximos tendrá tu artículo: "))
#temperatura = float(input("Del 1 al 10, qué tan creativo quieres que sea tu artículo: "))

#articulo_creado = contenido(tema, tokens, temperatura)
#print(articulo_creado)

#==================PARA RESUMIR UN ARTICULO=================
original = input("Elige el artículo a resumir: ")
tokens = int(input("Cuántos tokens máximos tendrá tu resumen: "))
temperatura = float(input("Del 1 al 10, qué tan creativo quieres que sea tu artículo: "))

resumen = resumir(original, tokens, temperatura)
print(resumen)