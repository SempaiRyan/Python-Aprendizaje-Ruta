# Bool contiene valores true o false
# tipos numericos, Falso para 0.True para 1

#Diccionario
valor={}
resul=bool(valor)
# print(f'Valor : {valor}, Resultado : {resul}')

valor={'Nombre: Juan , Apellido:Perez'}
result=bool(valor)
# print(f'Valor : {valor}, Resultado : {resul}')

variable=3

if bool(''):
    print('Regreso TRUEF')

else:
    print('Regreso Falso')

print('\n')

if '':
    print('Regreso TRUEF')

else:
    print('Regreso Falso')


while bool(variable) :
    print('Eje ciclo While')
    break
else:
    print('Fin Ciclo While')