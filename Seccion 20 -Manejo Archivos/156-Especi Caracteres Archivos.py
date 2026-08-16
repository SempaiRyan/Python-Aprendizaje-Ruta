try:
    archivo=open('prueba.txt','w',encoding='utf-8')

    # Agregar informacion
    archivo.write('Agg info del archivo uwu\n')

    archivo.write('Adios amigo mio UWU')


except Exception as e:

    print(e)

finally:

    archivo.close()

    print('Fin del archivo')

    # archivo.write('Nueva informacion')