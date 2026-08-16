# 82. Funciones Recursivas en Python
# Factorial de 5! =5x4x3x2x1
# 5!= 120


def factorial(numero):
    if numero==1:
        return 1

    else:
        return numero*factorial(numero-1)

resultado=factorial(5)
print(f'El factorial de 5 es : {resultado}')