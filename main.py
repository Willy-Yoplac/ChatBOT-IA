import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

#modelos = openai.Model.list()
#print(modelos)

modelo = "text-davinci-002"
prompt = "Cuentame una historia breve sobre un viaje a un pais europeo"

#Enviamos la peticon

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1, #Numero de respuestas que queremos
   # temperature =1, # que tan aleatorio seran las respuestas
    max_tokens = 100
)

texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)

print("*"*30) # diferenciar la respuesta tratada

# modelo que procesa informacion en español
modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

# paraque generar una pregunta sobre la entidad reconocida
ubicacion = None
for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break

# si existe la ubicacion
if ubicacion:
    prompt2 = f"Dime mas acreca de {ubicacion}"
    respuesta2 = openai.Completion.create(
        engine = modelo,
        prompt = prompt2,
        n=1,
        max_tokens =100
    )
    print(respuesta2.choises[0].text.strip())

