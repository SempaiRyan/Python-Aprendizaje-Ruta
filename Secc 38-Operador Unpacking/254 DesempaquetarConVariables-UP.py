# * desempaquetar
numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

# Desempaquetando al momento de pasar un parámetro a una función
def sumar(a, b, c):
    print(f'Resultado suma: {a + b + c}')

sumar(*numeros)

# Extraer algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a, *b, c, d = mi_lista
<<<<<<< HEAD
print(f"Lista : a,b,c,d")
=======
print(a,b,c,d)
>>>>>>> 3f68ce4c0892d5426c1fa39c2881a2ebb67e1397


