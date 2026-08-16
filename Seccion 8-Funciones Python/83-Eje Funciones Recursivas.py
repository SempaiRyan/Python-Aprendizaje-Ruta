# 83. Ejercicio Propuesto: Funciones Recursivas
#
# Imprimir numero de 5 a 1 de manera descendente usadno
# funciones recursivas
#
# Puede ser cualquier valor positivo , ejemplo ,
# si pasamos el valor de  5 , debe imprimir
# 5
# 4
# 3
# 2
# 1
# en caso de pasar el valor de 3
#
# 3
# 2
# 1
# Si se pasan valores negativos no imprimir nada

# 84. Solución Ejercicio Funciones Recursivas

def imprimir_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_recursivo(numero - 1)


    elif numero == 0:
        print("Llegamos a 0")

    
    else:
        print(f'El numero es incorrecto {numero}')


imprimir_recursivo(5)
