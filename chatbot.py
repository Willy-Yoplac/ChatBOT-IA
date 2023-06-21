import openai
import os
import spacy
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

preguntas_anteriores = []   #Se alamcenarán las preguntas que se hagan al ChatBot
respuestas_anteriores = []  #Se alamcenarán las respuestas que se hagan al ChatBot

#Cargamos el modelo spacy para trabajar en el idioma español
modelo_spacy = spacy.load("es_core_news_md")

#Creamos una lista con las palabras que deseamos censurar
palabras_prohibidas = ["lima", "unmsm", "universidad nacional mayor de san marcos"]

def filtrar_lista_negra(texto, lista_negra):
    token = modelo_spacy(texto)
    resultado = []

    for t in token:
        if t.text.lower() not in lista_negra:
            resultado.append(t.text)
        else:
            resultado.append("[XXXX]")
    
    return " ".join(resultado)


def preguntar_chat_gpt(prompt, modelo="text-davinci-002"):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1, #Numero de respuestas que queremos
        max_tokens = 150,
        temperature =1.5, # que tan aleatorio seran las respuestas
    )
    respuesta_sin_controlar = respuesta.choices[0].text.strip()
    respuesta_controlada = filtrar_lista_negra(respuesta_sin_controlar, palabras_prohibidas)
    return respuesta_controlada

print("Bienvenido a nuestro chatbot. Escribe 'salir' para finalizar.")

while True:
    conversacion = ""
    ingreso_usuario = input("\nTú: ")
    if ingreso_usuario == "salir":
        break

    for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion+=f"El usuario pregunta: {pregunta}\n"
        conversacion+=f"{respuesta}\n"

    prompt = f"El usuario pregunta: {ingreso_usuario}\n"
    conversacion += prompt #Se agrega la nueva pregunta a preguntas_anteriores
    respuesta_gpt = preguntar_chat_gpt(conversacion)
    print(f"ChatBot: {respuesta_gpt}")

    preguntas_anteriores.append(ingreso_usuario) #Se agregan las preguntas
    respuestas_anteriores.append(respuesta_gpt)  #Se agregan las respuestas