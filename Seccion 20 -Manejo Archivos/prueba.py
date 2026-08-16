# # # programa suma de 2 numeros
# # Dara error si en dicho programa el usuario da 1 numer y el otro
# # coloca una palabra ya que no es el caracter asignado para esto
#
# num1=int(input('Introduce un numero: '))
# num2=int(input('Introduce otro numero: '))
#
# resultado=num1+num2
# print(resultado)
#
#
# # Soluccion con la sentencias try y except
# #
# try:
#     num1=int(input('Introduce un numero: '))
#     num2=int(input('Introduce otro numero: '))
#     resultado=num1+num2
#     print(resultado)
#
# except :
#     print('Debes introducir numero obligatoriamente')

# Sentencia finally (eso se ejecuta si o si)


try:
    num1=int(input('Introduce un numero: '))
    num2=int(input('Introduce otro numero: '))
    resultado=num1+num2
    print(resultado)

except :
    print('Debes introducir numero obligatoriamente')
finally:
    print('Se ejecuta correctamente SI O SI')

# Control de las excepciones utilizando uyn bucle while

while (True):
    try:
        num1 = int(input('Introduce un numero: '))
        num2 = int(input('Introduce otro numero: '))
        resultado=num1+num2
        print(resultado)
        break
    except :
        print('Debes introducir numero obligatoriamente')