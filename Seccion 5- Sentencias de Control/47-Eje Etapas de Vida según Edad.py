edad=int(input("Proporciona Edad : "))
mensaje=None

if 0<= edad<10:
    mensaje="La infancia es GOD! "

elif 10<= edad<20:
    mensaje="Muchos cambios , estudios "

elif 20<= edad<30:
    print(f'Amor y trabajo trabajooo ....')

else:
    mensaje="Etapa de vida no reconocida"


print(f'Tu edad es{edad} , {mensaje}')

