# Profundizar python

#dar formato en str

nombre = 'Juan Junco'
edad = 28
sueldo = 30000

# mensaje_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
#
# print(mensaje_formato)
#
# mensaje='Nombre {0} , Edad {1}, Sueldo {2:.2f}  '.format(nombre, edad, sueldo)
#
# mensaje=' Sueldo {2:.2f},  Nombre {0} , Edad {1},  '.format(nombre, edad, sueldo)
#
# print(mensaje)
#
# mensaje='Nombre {n} , Edad{e} , Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)



diccionario = {
    'nombre': 'Ivan',
    'edad': 35,
    'sueldo': 30000
}

mensaje = 'Nombre:{dicc[nombre]} Edad:{dicc[edad]} Sueldo:{dicc[sueldo]:.2f}'.format(dicc=diccionario)
print(mensaje)
