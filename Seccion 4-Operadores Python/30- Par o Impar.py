# Este programa pide al usuario un número entero
a = int(input('Primeiro numero: '))

# Verifica si el número es divisible por 2
# Si el resto de la división es 0, significa que es par
if a % 2 == 0:
    print('Par')
else:
    # Si no es divisible por 2, entonces es impar
    print('Impar')

# Finalmente imprime "FIM" para indicar que el programa terminó
print('FIM')
