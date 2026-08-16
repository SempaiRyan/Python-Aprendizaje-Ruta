class Cubo:
    def __init__(self,alto,ancho,profundidade):
        self.alto=alto
        self.ancho=ancho
        self.profundidade=profundidade


    def calcularVolume(self):
        return self.alto*self.ancho*self.profundidade

#Crear los objetos
alto=int(input("Ingrese la alto: "))
ancho=int(input("Ingrese la ancho: "))
profundidade=int(input("Ingrese la profundidade: "))

#volumen
cubo1=Cubo(alto,ancho,profundidade)
print(f' El volumen Cubo :  {cubo1.calcularVolume() } ')
