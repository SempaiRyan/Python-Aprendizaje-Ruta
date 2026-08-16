# Profundizar python
from os.path import join

# help(str.join)

# JOIN = UNIR
# Tupla de Cadenas
tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
mensaje = ' '.join(tupla_str)   # <-- aquí agregamos un espacio como separador
print(f'Mensaje: {mensaje}')


# 2do ejemplos
list_cursop=['Java','Pyrthon','Angular','Spring']
mensaje=' '.join(list_cursop)
print(f'Mensaje: {mensaje}')

print('\n')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)   # aquí redefinimos mensaje
print(f'Mensaje: {mensaje}')


print('\n GG MANCO')
# Definir un diccionario con pares clave:valor
diccionario = {
    'nombre': 'Juan',
    'apellido': 'Perez',
    'edad': '18'
}

# Unir las llaves con guiones
llaves = '-'.join(diccionario.keys())

# Unir los valores con guiones
valores = '-'.join(diccionario.values())

print(f'llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, type: {type(valores)}')
