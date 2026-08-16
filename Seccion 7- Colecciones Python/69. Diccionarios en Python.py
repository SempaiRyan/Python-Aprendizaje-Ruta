dic={
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

# print(dic)
#
#
# # conocer cuantos elementos tiene  de largo
# print(len(dic))
#
# #Acceder a 1 elemento en diccionario (KEY)
#
# print(dic['IDE'])
#
# #Modificar elementos/ Se imprime el diccionario con el indice 0
# # pero el miniscula
# dic['IDE']='integrate development environment'
# print(dic)

# 70. Diccionarios en Python - parte 2
# En Python, el método .items() se utiliza con diccionarios para
# obtener una vista de todos los pares clave-valor
# en forma de tuplas.

for termino, valor in dic.items():
    print(termino,valor)

for termino in dic.keys():
    print(termino)

for valor in dic.values():
    print(valor)

print ('IDE' in dic)

#Agregar un elemento
dic['PK']='PRIMARY KEY'
print(dic)

#Remover un elemento
dic.pop('DBMS')
print(dic)

#Limpiar
dic.clear()
print(dic)

# #eliminar dic
# del dic
# print(dic)