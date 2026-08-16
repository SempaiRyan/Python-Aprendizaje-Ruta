#Definir tuplas

fruta=('Naranja','Platano','Guayaba')

#Saber el largo de la tupla

print(len(fruta))


#Acceder a un elemento
print(fruta[0])


#Navegacion inversa
print(fruta[-1])

#Acceder a un rango, sin incluir en ultimo indice
print(fruta[0:2])


# 65. Tuplas en Python - parte 2
for n in fruta:
    print(n , end=' ..')

#Cambiar valor tupla , es inmutable
# fruta[0]='Pera'
# print(fruta)

frutaLista=list(fruta)
frutaLista[0]='Pera'
fruta=tuple(frutaLista)
print('\n',fruta)




