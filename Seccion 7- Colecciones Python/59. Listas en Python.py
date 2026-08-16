# # 59. Listas en Python
names=['Juan','Carlos','Ibeth','Dariel','Thiago','Geoconda','Tariel','Nathaly']

# Imprimir la lista de nombre con numero
print(f'El Indice esta en dato : {names}')


#Acceder al elemento de la lista en especifico
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print("///////////")



# 60. Listas en Python - parte 2
#Se imprime un rango , sin incluir el indice 2
print(names[:2])


print(names[-1])
#De atras para adelante

#Cambiar un valor
names[3]='Ivone'
print(names[3])
print("///////////")
print("///////////")
print("///////////")
## ITERAR NUESTRA LISTA
for name in names:
    print(name)
else:
    print("No existe nombre en lista")

print("///////////")
print("///////////")
print("///////////")

# 61. Listas en Python - parte 3
#preguntar largo de una lista

#Len cantidad de elementos en la lista
print(len(names))


#Agregar elemento en la lista
names.append('Lorenzo')
print(names)


#Insertar un elemento en un indice especifico
names.insert(1,'OCTAVIO')
print(names)

#Remover un elemento
names.remove('OCTAVIO')

names.remove('Carlos')

names.remove('Ibeth')
print(names)

#Remover el ultimo valor agregado
#El ultimo valor es Lorenzo
names.pop()
print(names)

#Eliminar indice especifico
#Se elimina el indice Juan
del names[0]
print(names)


#Limpiar toda la lista
names.clear()
print(names)

#Borrar lista completo
del names
print(names)