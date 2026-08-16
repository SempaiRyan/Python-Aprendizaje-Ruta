num=int(input("Ingrese un numero entre 1 a 3 : "))

numText=''
if num==1:
    numText="Numero 1no"
elif num==2:
    numText="Numero 2no"
elif num==3:
    numText="Numero 3no"
else:
    numText="Valor Fuera de Rango"

print(f'Numero Proporcionado {num}---{numText}')