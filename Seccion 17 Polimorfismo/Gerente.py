from Empleados import *

class Gerente (Empleado):
    def __init__(self, nombre, sueldo,departamento):
        #Herencia del padre
        super().__init__(nombre, sueldo)

        #Iniciacion de atributo hijo
        self.departamento = departamento

    def __str__(self):
        return f'Gerente : [Departamento :{self.departamento}+   Herencia: {super().__str__()}'

    # def mostrar_Detalles(self):
    #     return self.__str__()