
class MiClase:

    variable_clase='Valor variable CLASE'

    def __init__(self, valor_variable):

        self.variable_instancia = valor_variable



miClase = MiClase('Valor variable INSTANCIA')
print(MiClase.variable_clase)
print(miClase.variable_instancia)


print('\n')

miClase2 = MiClase('Otra variable Instancia ')
print(miClase2.variable_clase)
print(miClase2.variable_instancia)



























