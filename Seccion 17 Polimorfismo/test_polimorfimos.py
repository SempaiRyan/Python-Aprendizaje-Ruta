# from Empleados import *
# from Gerente import *
#
# def imprimir_Detalles(objeto):
#
#     print(type(objeto))
#     print(objeto.mostrar_Detalles())
#
# empleado1=Empleado('Juan',5000)
# imprimir_Detalles(empleado1)
#
# print('\n')
#
# gerente1=Gerente('Juan',5000,'Sistemas Informaticos (TICS)')
# imprimir_Detalles(gerente1)



# 142- METODOINSTANCIA Y POLIMORFIMOS EN PYTHONB

from Empleados import *
from Gerente import *

def imprimir_Detalles(objeto):

    print(type(objeto))
    print(objeto.mostrar_Detalles())

    #Para saber el metodo de cierta clases
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado1=Empleado('Juan',5000)
imprimir_Detalles(empleado1)

print('\n')

gerente1=Gerente('Juan',5000,'Sistemas Informaticos (TICS)')
imprimir_Detalles(gerente1)
