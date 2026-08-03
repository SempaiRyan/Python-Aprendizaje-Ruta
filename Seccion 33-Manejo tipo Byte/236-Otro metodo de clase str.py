# Leer contenido online
import urllib
from urllib.request import urlopen

palabras=[]
# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

with urlopen(peticion) as mensaje:
    contenido = mensaje.read().decode('utf-8')

#contar ocurrencia de una cadena
print('Num Veces Palabra Universiodad:  ',contenido.count('Universidad'))

# Upper conviener a mayuscula un str
print(contenido.upper())

# Upper Convierte en minuscula
print(contenido.lower())

# buscamos la cadena python en el contenido
print('python'.lower() in contenido.lower())

print('Existe python?: ','python'.lower() in contenido.lower())

print('Existe python?: ','python'.upper() in contenido.upper())


# startswitch -inici con

print('Inicia con : startswitch ',contenido.startswith('En GlobalMentoring.com.mx'))



# endswith -termina con
print('Termina con : ',contenido.endswith('GlobalMentoring.com.mx'))
print('Termina con : ',contenido.lower().endswith('globalmentoring.com.mx'.lower()))
















