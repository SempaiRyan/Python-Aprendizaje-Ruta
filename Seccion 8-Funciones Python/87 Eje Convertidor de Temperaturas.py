# # 87. Ejercicio Propuesto: Convertidor de Temperaturas
#
# Convertir la temperatura
# Realizar 2 funciones para
# convertir de grados celsius a fahrenhetit y viceversa.


def celcius_to_fahrenheit(celcius):
    return celcius * 9/5+ 32


# funcion convertir fahrenheit a celcius
def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32)*5/9

#realizar pruebas de conversion
celcius=float(input('Proporciona Celcius : '))
resultado=celcius_to_fahrenheit(celcius)

#imprimir resultado
print(f'{celcius} C a F : {resultado:.2f} F')




#imprimimos resultados
fahrenheit=float(input('Proporciona Fahrenheit : '))
resultado=fahrenheit_to_celcius(fahrenheit)
print(f'{fahrenheit} C a F : {resultado:0.2f} F')
