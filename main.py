import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

#modelos = openai.Model.list()
#print(modelos)

modelo = "text-davinci-002"
prompt = "¿Cúal es la capital de Francia?"
#prompt = input("Ingresa tu pregunta: ")

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1 #Numero de respuestas que queremos
)
texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)