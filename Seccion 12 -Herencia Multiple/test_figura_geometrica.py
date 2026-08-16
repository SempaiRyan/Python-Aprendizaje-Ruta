from Cuadrado117 import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Color import Color
from Rectangulo import Rectangulo


print(f'{"--"*10}***CREACCION OBJETOS Cuadrado{"--"*10}')


cuadrado1=Cuadrado(5,'Rojo')
cuadrado1.alto=9
cuadrado1.ancho=9
print(f'Ancho: {cuadrado1.ancho},'
      f' Alto: {cuadrado1.alto}, Color: {cuadrado1.color}')

print(f'El área calculada es: {cuadrado1.calcularArea()}')
print(cuadrado1)


# # 119. Método MRO - Method Resolution Order en Python
# print(Cuadrado.mro())



print(f'{"--"*10}***CREACCION OBJETOS Rectangulo{"--"*10}')

rectangulo1=Rectangulo(9,8,'Cafe Oro')
rectangulo1.ancho=15

print(f'Area del Rectangulo es :{rectangulo1.calcularArea()},')
print(rectangulo1)
print(cuadrado1.mro())
