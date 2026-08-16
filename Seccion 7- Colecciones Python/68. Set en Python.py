planeta={'Marte','Venus','Jupiter'}
print(planeta)

#Largo
print(len(planeta))

#REvisa si un elemento esta presente
print('Marte' in planeta)

# Agregar un elemento
planeta.add('Tierra')
print(planeta)

#No se puede duplicar elemento
planeta.add('Tierra')
# print(planeta)
# {'Marte', 'Venus', 'Tierra', 'Jupiter'}

#Eliminar elemento
planeta.remove('Tierra')
print(planeta)

#Eliminar elemento sin arrojar error
planeta.discard('Jupiters')
print(planeta)

#limpiar set
planeta.clear()
print(planeta)

#Eliminar set
del planeta
print(planeta)