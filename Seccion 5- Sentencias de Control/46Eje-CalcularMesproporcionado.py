mes=int(input("Proporciona mes del Year 1 a 12 : "))
esta=None #None es Null
if mes==1 or mes==2 or mes==12:
    esta="Invierno"
elif mes==3 or mes==4 or mes==5:
    esta="Primaveras :)"

elif mes==6 or mes==7 or mes==8:
    esta="Verano"

elif mes==9 or mes==10 or mes==11:
    esta="Otonos"
else:
    esta="Mes Incorrecto estimados"

print(f'Para mes  {mes} la estacion es : {esta}')

