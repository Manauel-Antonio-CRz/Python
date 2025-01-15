from googletrans import Translator

def traducir_texto(texto, idioma_destino="es"):
    translator = Translator()
    traduccion = translator.translate(texto, dest=idioma_destino)
    return traduccion.text

texto = input("Escribe el texto que deseas traducir: ")
idioma = input("¿A qué idioma deseas traducirlo? (por ejemplo, 'es' para español): ")
print("Traducción:", traducir_texto(texto, idioma))
