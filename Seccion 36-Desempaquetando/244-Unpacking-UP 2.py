# Unpacking - desempaquetado
valores = 1,2,3

print(valores)
print(type(valores))

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

valor1, _, valor3 = 1, 2, 3
print(valor1, valor3)

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)

print('\n')
print('\n')
print('\n')
valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))


def regresa_Datos():

    return 1,2,3


print(regresa_Datos())

valor1,valor2,valor3=regresa_Datos()

print(valor1, valor2, valor3)



valor1,*_=regresa_Datos()

print(valor1,_)

















