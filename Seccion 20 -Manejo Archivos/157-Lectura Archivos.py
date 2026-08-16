
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
print(archivo.read())

















