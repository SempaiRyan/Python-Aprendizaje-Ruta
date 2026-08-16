import psycopg2 as bd

conexion = bd.connect(

    user="postgres",

    password="2010",

    host="localhost",

    port="5432",

    database="test_db"
)


try:

    #Guardar de manera automatica NO
    conexion.autocommit=False

    cursor = conexion.cursor()
    sentencia='INSERT INTO persona(nombre,apellido,mail) VALUES (%s,%s,%s)'
    valores=('Carla','Lara','clara@gmail.com')
    cursor.execute(sentencia,valores)



    sentencia='UPDATE persona SET nombre=%s, apellido=%s, mail=% WHERE idpersona=%s'
    valores=('Juan Carlos','Juarez','jcjuarez@gmail.com',18)
    cursor.execute(sentencia,valores)

    conexion.commit()
    print('Termina la transacion, se hizo COMMIT')

except Exception as e:

    conexion.rollback()

    print(f'Ocurrió un error , se hizo RollBack amigos {e}')

finally:

    conexion.close()
