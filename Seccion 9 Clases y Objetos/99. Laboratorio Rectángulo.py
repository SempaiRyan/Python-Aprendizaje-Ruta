class Rectangulo:


    def __init__(self,base,altura):
        self.base=base
        self.altura=altura


    def area(self):
        return self.base*self.altura

#Objetos
base=int(input('Proporciona la base : '))
altura=int(input('Proporciona la altura : '))
retangulo1=Rectangulo(base,altura)
print(f'Area del rectangulo : { retangulo1.area() }')


