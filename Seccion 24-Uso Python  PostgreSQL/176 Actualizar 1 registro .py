import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="2010",
    host="localhost",
    port="5432",
    database="test_db"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s  ,mail=%s WHERE id_persona=%s '
            valores = (

                ('Juan', 'Perez', 'jperez@gmail.com', 1),
                ('Ivonne', 'Gutierrez', 'igutierrez@gmail.com', 2)


            )


            cursor.executemany(sentencia, valores)

            registro_actualizados = cursor.rowcount
        print(f'Registro Actualziados  : {registro_actualizados}')

except Exception as e:
    print(f'Ocurrió un error {e}')

finally:
    conexion.close()
