# 10/0
# # ZeroDivisionError

# Esto en otros lenguajes es un try/catch
# Variables
resultado=None

a='10'
b=0

try:

    resultado = a/b
except Exception as e:
    print(f'Ocurrio Error: {e}')

print(f'Resultado: {resultado}')
print('Continuamos.....')



# BaseException → Clase base de todas las excepciones en Python
# Exception → Clase base para la mayoría de errores comunes

# ArithmeticError → Errores relacionados con operaciones matemáticas
# ZeroDivisionError → División entre cero

# OSError → Errores relacionados con el sistema operativo
# FileNotFoundError → Archivo no encontrado
# PermissionError → Permisos insuficientes para acceder a un archivo

# RuntimeError → Errores detectados durante la ejecución que no encajan en otras categorías

# LookupError → Errores al buscar elementos en colecciones
# IndexError → Índice fuera de rango en listas/tuplas
# KeyError → Clave inexistente en diccionarios

# SyntaxError → Error de sintaxis en el código
# IndentationError → Error de indentación (espacios/tabs incorrectos)
