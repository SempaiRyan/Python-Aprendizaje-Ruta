# 126. Variables de Clase en Python

class MiClase:
    #variable de clase
    variable_clase= 'Valor variable clase'


    #Variable de Instancia
    def __init__(self, variable_instancia):
        self.variable_instancia=variable_instancia


#metodos de clase
# Metodo estaticos python(staticmethod)

    @staticmethod
    #Decorador
    def metodo_estatico():
        print (MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print (cls.variable_clase)

    def metodo_Instancias(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)



MiClase.metodo_estatico()
miObjeto1=MiClase('Valor variable Instancias')
miObjeto1.metodo_clase()
miObjeto1.metodo_estatico()

miObjeto1.metodo_Instancias()


