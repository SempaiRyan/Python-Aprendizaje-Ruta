# 126. Variables de Clase en Python

class MiClase:
    #variable de clase
    variable__clase= 'Valor variable clase'


    #Variable de Instancia
    def __init__(self, variable_instancia):
        self.variable_instancia=variable_instancia

print(MiClase.variable__clase)
miClase=MiClase('Valor variable instancias')
print(miClase.variable_instancia)
print(miClase.variable__clase)

miClase2=MiClase('OTRO Valor variable instancias')
print(miClase2.variable_instancia)
print(miClase2.variable__clase)