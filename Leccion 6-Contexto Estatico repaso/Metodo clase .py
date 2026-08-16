class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    #Metodo estatico
    @staticmethod
    def metodo_estaticos():
        print(MiClase.variable_clase)

    #Metodo Clase
    @classmethod
    def metodo_classe(cls):
        print(cls.variable_clase)



MiClase.metodo_estaticos()