import psycopg2

conexion = psycopg2.connect(
    user="postgres1",
    password="2010",
    host="localhost",
    port="5432",
    database="test_db"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia='DELETE FROM persona WHERE id_persona IN %s'
            entrada=input('Proporciona ID_PERSONA a eliminar (separado por comas) : ')
            valores=(tuple(entrada.split(',')),)


            cursor.execute(sentencia, valores)

            registros_eliminados = cursor.rowcount

        print(f'Registro Eliminados  : {registros_eliminados}')


except Exception as e:
    print(f'Ocurrió un error {e}')

finally:
    conexion.close()
