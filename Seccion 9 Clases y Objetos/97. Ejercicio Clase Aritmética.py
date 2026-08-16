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

#Objeto de la clase
aritmetica1=Aritmetica(5,3)

print(aritmetica1.sumar())