try:
    archivo=open('prueba.txt','w')

    # Agregar informacion
    archivo.write('Agg info del archivo uwu\n')
    archivo.write('Adios amigo mio UWU')

except Exception as e:
    print(e)
finally:
    archivo.close()