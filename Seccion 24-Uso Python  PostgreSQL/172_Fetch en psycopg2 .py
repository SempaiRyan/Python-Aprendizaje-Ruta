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
            # Placeholder correcto: %s (minúscula)
            sentencia = 'SELECT * FROM persona WHERE id_persona =%s'
            id_persona = input('Introduce el valor  Id_persona: ')

            # Pasar parámetros como tupla
            cursor.execute(sentencia, (id_persona,))

            registros = cursor.fetchone()  # Recuperar registros
            print(registros)

except Exception as e:
    print(f'Ocurrió un error {e}')

finally:
    conexion.close()
