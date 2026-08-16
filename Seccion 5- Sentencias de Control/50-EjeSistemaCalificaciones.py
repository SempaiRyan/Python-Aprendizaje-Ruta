# Instrucciones de la tarea:
# El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
# El usuario proporcionará un valor entre 0 y 10.
# Si está entre 9 y 10: imprimir una A
# Si está entre 8 y menor a 9: imprimir una B
# Si está entre 7 y menor a 8: imprimir una C
# Si está entre 6 y menor a 7: imprimir una D
# Si está entre 0 y menor a 6: imprimir una F
# Cualquier otro valor debe imprimir: Valor incorrecto
# Ejemplo:
# Proporciona un valor entre 0 y 10:
# A

Califi=int(input('Calificaciones de entre 0 a 10 : '))

if 9<= Califi <=10:
    print(f'Puntaje A')
elif 8<= Califi <9:
    print(f'Puntaje B')
elif 7<= Califi <8:
    print(f'Puntaje C')
elif 6<= Califi <7:
    print(f'Puntaje D')
elif 0<= Califi <6:
    print(f'Puntaje E /Reprobado ')
else:
    print(f'Puntaje Incorrectos')