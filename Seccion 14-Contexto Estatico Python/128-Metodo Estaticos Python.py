# 126. Variables de Clase en Python

class MiClase:
    #variable de clase
    variable_clase= 'Valor variable clase'


    #Variable de Instancia
    def __init__(self, variable_instancia):
        self.variable_instancia=variable_instancia


#metodos de clase
# 18-Metodo estaticos python(staticmethod)

    @staticmethod
    #Decorador
    def metodo_estatico():
        print (MiClase.variable_clase)



MiClase.metodo_estatico()







