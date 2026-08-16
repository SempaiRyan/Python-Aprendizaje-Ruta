name=input('Ingrese tu nombre : ')
print(name)

id=int(input('Ingrese tu id : '))
print(id)

precio=float(input('Ingrese precio : '))
print(precio)

envio=input('Ingrese envio True-False :')

if envio=="True":
    envio=True

elif envio=="False":
    envio=False
else:
    print("Valor incorrecto")