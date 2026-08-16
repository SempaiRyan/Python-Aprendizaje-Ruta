# manejo de contexto
# With = con

#with open('prueba.txt','r',encoding='utf-8') as archivo:

from ManejoArchivos import ManejoRecursos

# Usamos el administrador de contexto
with ManejoRecursos('pruebas.txt') as archivo:

    print(archivo.read())




