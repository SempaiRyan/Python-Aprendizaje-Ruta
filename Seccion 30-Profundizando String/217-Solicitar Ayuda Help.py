# Profundizar python
# import math
#
#
# help(math.isnan)
#
# help(str.capitalize)

# 218
# from mi_clase import MiClase
# help(MiClase)
#
# print(MiClase.__doc__)
#
# # Detalle metodo init
#
# print(MiClase.__init__.__doc__)
# print(MiClase.__doc__)
#
# print(MiClase.mi_metodo.__doc__)
# print(MiClase.mi_metodo)
# print(type(MiClase.mi_metodo))



# 219 Str son inmutables
# help(str.capitalize)

men1='hola mundos'
men2=men1.capitalize()
print(men2)
print(f'mensaje 1 {men1} , id 1: {id(men1)}')
print(f'mensaje 2 {men2} ,id 2: {id(men2)}')
men1 +='adios'
print(f'mensaje 1 {men1} , id 1: {hex(id(men1))}')






