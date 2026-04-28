edad=int(input("Escribe tu edad: "))


"""
veintes=edad >=20 and edad <30
print(veintes)

treintas=edad>=30 and edad <40
print(treintas)
"""

if (edad >=20 and edad <30) or (edad>=30 and edad <40):
    print("Dentro de Rango 20s o 30s")

    """
    if veintes:
        print("Dentro de Rango 20s")
    elif treintas:
        print("Dentro de Rango 30s/")
    else:
        print("Fuera ")
  """
else:
    print("Fuera de rangos de 20s o 30s")