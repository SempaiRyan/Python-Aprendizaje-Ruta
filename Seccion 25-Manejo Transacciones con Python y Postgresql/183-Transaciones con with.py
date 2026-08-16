import psycopg2 as bd

conexion = bd.connect(
    user="postgres",
    password="2010",
    host="localhost",
    port="5432",
    database="test_db"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # INSERT
            sentencia = 'INSERT INTO persona(nombre, apellido, mail) VALUES (%s, %s, %s)'
            valores = ('Alex', 'Rogas', 'arogas@gmail.com')
            cursor.execute(sentencia, valores)

            # UPDATE
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, mail=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Perez', 'jperez@gmail.com', 1)
            cursor.execute(sentencia, valores)

            conexion.commit()
            print('Termina la transacción, se hizo COMMIT')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo RollBack amigos: {e}')

finally:
    conexion.close()
