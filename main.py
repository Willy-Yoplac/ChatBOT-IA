import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

#modelos = openai.Model.list()
#print(modelos)

modelo = "text-davinci-002"
prompt = "Elija un buen nombre para un perrito"
#prompt = input("Ingresa tu pregunta: ")

#Enviamos la peticon

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=3, #Numero de respuestas que queremos
    temperature =1, # que tan aleatorio seran las respuestas
    max_tokens = 50
)

for idx, opcion in enumerate(respuesta.choices):
    text_generado = opcion.text.strip()
    print(f'Respuesta {idx + 1}: {text_generado}\n')