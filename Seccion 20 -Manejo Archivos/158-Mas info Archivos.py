
# "r"  -
# Read: abre un archivo para lectura (por defecto). Error si no existe.

# "a"  -
# Append: abre un archivo para añadir contenido. Crea el archivo si no existe.

# "w"  -
# Write: abre un archivo para escritura. Crea el archivo si no existe.

# "x"  -
# Create: crea un archivo nuevo. Error si ya existe.

# "t"  - Text: modo texto (por defecto).
# "b"  - Binary: modo binario (ej. imágenes).



# archivo = open('C:\\Users\\Carlos\\Desktop\\Python-Aprendizaje-Ruta\\Seccion 20 -Manejo Archivos\\prueba.txt','r')

archivo = open('prueba.txt','r')
# print(archivo.read())



# Leer algunso caracteres
# print(archivo.read(20))
# print(archivo.read(10))



# Leer Lineas completas
# print(archivo.read())



# Iterar el archivo
# for linea in archivo:
#     print(linea)


# Leer todas las lineas - Nos viene en una lista
# print(archivo.readlines())


# Acceder a 1 linea de la lista
# print(archivo.readlines()[1])


# Abrimos un nuevo archivo
# a- Anexar informacion

archivo2=open('copia.txt','a',encoding='utf-8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se termino proceso Leer y copiar Archivo')




































