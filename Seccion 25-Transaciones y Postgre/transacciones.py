import psycopg2
import psycopg2 as bd

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
            cursor = conexion.cursor()

            sentencia = 'INSERT INTO personas (id_persona, nombre, apellido, mail) VALUES (%s, %s, %s, %s)'
            valores = (7, 'Alex', 'Rojas', 'arojas@gmail.com')
            cursor.execute(sentencia, valores)

            sentencia='UPDATE personas SET nombre=%s,apellido=%s,mail=%s WHERE id_persona=%s'
            valores=('Juan','Perez','jperez@gmail.com',1)
            cursor.execute(sentencia, valores)


except Exception as e:
    conexion.rollback()
    print(f'Error , se hizo rollback  {e}')

finally:
    print('Termina Transaciones, se hizo commit')

    conexion.close()
