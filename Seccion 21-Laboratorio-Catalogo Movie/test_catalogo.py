from Domi import Pelicula
from CatalogoPelicula.Servis.CatalogoPelicula import CatalogoPeliculas
CatalogoPeliculas

cp = CatalogoPeliculas()

op = None
while op != 4:
    try:
        print('Opciones : ')
        print('1 - Agregar Pelicula')
        print('2 - Listar Pelicula')
        print('3 - Eliminar Pelicula')
        print('4 - Salir')
        op = int(input('Escribe una opcion: 1 al 4 : '))

        if op == 1:
            nombre_pelicula = input('Ingresa el nombre de la Pelicula: ')
            pelicula = Pelicula (nombre_pelicula)
            cp.agregar_pelicula(pelicula)  # aquí ya se crea/actualiza peliculas.txt


        elif op == 2:
            cp.listar_pelicula()

        elif op == 3:
            cp.eliminar_pelicula()

    except Exception as e:
        print(f'Ocurrió error {e}')
        op = None

else:
    print('SALIMOS DEL PROGRAMA')