class Vehiculos:

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas


    def __str__(self):
        return f'Vehi Color :{self.color} + Cantidad Ruedas: {self.ruedas}'


class Coche(Vehiculos):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad


    def __str__(self):
        return f'{super().__str__()} +  Velocidad Km/h : {self.velocidad}'




class Bicicleta(Vehiculos):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()} +Tipo Bici: {self.tipo}'





#objetos de clase Padre Vehiculo
vehiculo1=Vehiculos('Rojo',5)
print(vehiculo1)


#objeto clase hija
coche1=Coche('Azul Cielo','3',120)
print(coche1)

#objeto clase hija
bici1=Bicicleta('Gris Marron','2','Competitivo')
print(bici1)