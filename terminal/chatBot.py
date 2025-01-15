import re

import pyttsx3 # pip install pyttsx3
from nltk.chat.util import Chat, reflections  # pip install nltk

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Configurar el volumen y velocidad de la voz
engine.setProperty('volume', 3)  # Rango de 0.0 a 1.0
engine.setProperty('rate', 150)  # Velocidad de la voz


# Función para hablar el texto
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()


# Definir los pares de conversación del chatbot
pares = [
    (r"Hola", ["¡Hola!", "¿Cómo puedo ayudarte?"]),
    (r"Como estas", ["Estoy bien, gracias por preguntar.", "Estoy funcionando correctamente."]),
    (r"Adiós", ["¡Adiós!"]),
    (r"como te llamas", ["ada"]),
    (r"a que se deve ese nombre", ["Fue la primera programadora al saber que los números también son para música y artes, entre otras cosas. De ahí se inspiró mi nombre"])
]


# Función principal del chatbot
def chatbot():
    print("¡Hola! Soy tu chatbot. (Escribe 'salir' para terminar)")
    while True:
        usuario = input("Tú: ")
        if usuario.lower() == 'salir':
            hablar("¡Adiós!")
            break

        for pattern, responses in pares:
            if re.match(pattern, usuario):
                respuesta = responses[0]
                print(f"ADA: {respuesta}")
                hablar(respuesta)
                break


# Iniciar el chatbot
chatbot()
