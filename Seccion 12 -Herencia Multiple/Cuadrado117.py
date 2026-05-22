from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):

        #super()__init__(lado)
        #init nivel de la clase
        #Herencia Multiple Python Exacta
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)




    #Accedemos a los atributos de la class Padre FiguraGeometrica
    def calcularArea(self):
        return self.alto*self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}{Color.__str__(self)}'




