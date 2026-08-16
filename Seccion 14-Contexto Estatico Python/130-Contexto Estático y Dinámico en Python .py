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

# 130. Contexto Estático y Dinámico en Python
MiClase.metodo_estatico()







