# Crear una función que reciba múltiples
# valores numéricos utilizando *args

# y regrese como resultado la multiplicación de todos los
# valores pasados como argumentos.

#Definir funcion para multiplicar valores}

def multiplicar(*numeros):
    resultado=1

    for numero in numeros:
        resultado*=numero
    return resultado

#llamar la funcion
print(multiplicar(3,5,15))
