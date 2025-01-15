import  random
import  string
def generador_contraseña(longitud=8): #lo puede modifical al numero que quiera
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for i in range(longitud))

print(generador_contraseña(16))