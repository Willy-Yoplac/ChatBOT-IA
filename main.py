import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

#modelos = openai.Model.list()
#print(modelos)

modelo = "text-davinci-002"
prompt = "Escribe oraciones con la palabra 'casa'."
#prompt = input("Ingresa tu pregunta: ")

#Enviamos la peticon

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=2, #Numero de respuestas que queremos
    temperature =0.5, # que tan aleatorio seran las respuestas
    max_tokens = 100
)

for idx, opcion in enumerate(respuesta.choices):
    text_generado = opcion.text.strip()
    print(f'Respuesta {idx + 1}: {text_generado}\n')