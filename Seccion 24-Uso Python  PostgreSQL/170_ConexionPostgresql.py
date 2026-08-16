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

            sentencia = 'SELECT * FROM persona WHERE persona.id_persona = %S'


            cursor.execute(sentencia)

            registros = cursor.fetchall()  # Recuperar registro de la sentencia

            print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')

finally:

    conexion.close()
