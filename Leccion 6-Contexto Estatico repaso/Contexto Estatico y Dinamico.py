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
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodoinstancia(self):
        self.metodo_clase()
        self.metodo_estaticos()
        print(self.variable_clase)
        print(self.variable_instancia)


MiClase.metodo_estaticos()

objeto1=MiClase('Variable variable instancias')
objeto1.metodo_clase()
objeto1.metodoinstancia()



