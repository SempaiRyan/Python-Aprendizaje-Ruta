# 126. Variables de Clase en Python

class MiClase:
    #variable de clase
    variable_clase= 'Valor variable clase'


    #Variable de Instancia
    def __init__(self, variable_instancia):
        self.variable_instancia=variable_instancia


print(MiClase.variable_clase)
#objeto
miClase=MiClase('Valor Variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

MiClase.variable_clase2='Valor variable clase 2'


miClase2=MiClase('Otra valor variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

print(MiClase.variable_clase2)
print(miClase2.variable_clase2)