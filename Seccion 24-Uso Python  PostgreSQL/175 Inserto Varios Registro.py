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
            sentencia='INSERT INTO persona(nombre,apellido,mail) VALUES (%s,%s,%s) '
            valores=(

                ('Marco','Cantu','mcantu@gmail.com'),
                ('Angel', 'Quintana', 'aquitana@gmail.com'),
                ('Maria', 'Gonzales', 'mgonzales@gmail.com')


            )
            cursor.executemany(sentencia,valores)

            #conexion.commit()

            registro_insertados=cursor.rowcount
            print(f'Registro Insertados : {registro_insertados}')

except Exception as e:
    print(f'Ocurrió un error {e}')

finally:
    conexion.close()
