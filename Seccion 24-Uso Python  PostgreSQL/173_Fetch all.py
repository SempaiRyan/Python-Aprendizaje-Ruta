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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            #id_persona = input('Introduce el valor  Id_persona: ')


            entrada=input('Proporciona ID a buscar: ')
            llaves_primarias=(tuple(entrada.split(',')),)     #Eliminar las comas

            # Pasar parámetros como tupla
            cursor.execute(sentencia,llaves_primarias)

            registros = cursor.fetchall()  # Recuperar registros

            for registro in registros:
                print(registros)

except Exception as e:
    print(f'Ocurrió un error {e}')

finally:
    conexion.close()
