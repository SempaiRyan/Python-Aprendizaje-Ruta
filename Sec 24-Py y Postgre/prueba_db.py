import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="2010",
    host="localhost",
    port="5432",
    database="test_db"
)

try:
    with (conexion):
        with conexion.cursor() as cursor:
            # INSERT
            # sentencia = 'INSERT INTO personas (id_persona, nombre, apellido, mail) VALUES (%s, %s, %s, %s)'
            # valores = (
            #     (4,'Marcos', 'Cantu', 'mcantu@gmail.com'),
            #     (5,'Angel', 'Quinta', 'aquinta@gmail.com'),
            #     ( 6,'Maria', 'Gonza', 'mgonzales@gmail.com')
            #
            # )



            # ='UPDATE personas SET nombre=%s,apellido=%s,mail=%s WHERE id_persona=%s'
            # valores=(
            #     ('Juan','Juarez','jjuarez@gmail.com',1),
            #     ('Ivon', 'Guiti', 'iguiti@gmail.com', 2)
            # )

            # Delete 1 registro
            # sentencia='DELETE FROM personas WHERE id_persona=%s'
            # valores=(6,)

            sentencia='DELETE FROM personas WHERE id_persona IN %s'
            entrada=input('ID PARA ELIMINAR : ')
            valores =(tuple(entrada.split(',')),)

            cursor.execute(sentencia, valores)
            registro_delete = cursor.rowcount

            print(f'Registro eliminado  : {registro_delete}')

except Exception as e:
    print(f'Error {e}')

finally:
    conexion.close()
