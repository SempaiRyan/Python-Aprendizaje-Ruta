# def sumar (a,b):
# 	return a+b
#
# resultado = sumar(3,4)
#
#
# print(f'Resultado: {resultado}')
#
# print(f'Resultado: {resultado 3+4=7}')

# 74. Valores por Default en los Parámetros de una Función


def sumar (a=0,b=0)->int:
	return a+b

resultado = sumar()


print(f'Resultado: {sumar}')
print(f'Resultado: {sumar(2,8)}')