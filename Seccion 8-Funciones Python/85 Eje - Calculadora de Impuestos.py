# Ejercicio: Calculadora de Impuestos
# Crear una función para calcular el total de
# un pago incluyendo un impuesto aplicado.

# Fórmula: pago_total = pago_sin_impuesto + pago_sin_impuesto
# * (impuesto/100)


#Funciones que calcula el total de un pago incluyendo el impuesto


def calcular_impuesto(pagoSinImpuesto,impuesto):
    pago_total=pagoSinImpuesto+pagoSinImpuesto*(impuesto/100)
    return pago_total

# Ejecutamos la funcion
pagoSinImpuesto=float(input("Ingrese valor sin impuesto :"))
impuesto=float(input("Ingrese valor del impuesto :"))

pagoConImpuesto=calcular_impuesto(pagoSinImpuesto,impuesto)


print(f'Pago con Impuesto : {pagoConImpuesto}')