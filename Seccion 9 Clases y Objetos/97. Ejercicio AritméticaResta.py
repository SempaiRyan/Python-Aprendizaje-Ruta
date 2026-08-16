class Aritmetica:
    """
    CLASE ARITMETICA PARA REALIZAR OP SUM,RESTA ETC


    """

    #METODO dunder=double underscore (doble guin bajo)
    def __init__(self,opeA,opeB):
        self.opeA=opeA
        self.opeB=opeB

    def sumar(self):
        return self.opeA+self.opeB

    def resta(self):
        return self.opeA-self.opeB


    def multiplicar(self):
        return self.opeA*self.opeB

    def dividir(self):
        return self.opeA/self.opeB
#Objeto de la clase
aritmetica1=Aritmetica(5,3)

print(f'Suma es : {aritmetica1.sumar()}')
print(f'Resta es :  {aritmetica1.resta()}')

print(f'Multiplo : {aritmetica1.multiplicar()}')
print(f'Dividir : {aritmetica1.dividir():0.2f}')