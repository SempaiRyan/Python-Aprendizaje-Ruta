# v81. Distintos tipos de datos como argumentos en Python


def despejarNombre(nombres):
    for nombre in nombres:
        print(nombre)

nombres=['Juan','Karl','Guillen']
despejarNombre(nombres)
despejarNombre('Carlos')
despejarNombre((10,11))

despejarNombre([15,16])