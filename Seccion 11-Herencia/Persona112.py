class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad


    def __str__(self):
        return f'Persona Nombre:{self.nombre} Edad:{self.edad} '




#Herencia = clase hija

class Empleado(Persona):

    def __init__(self,nombre,edad,sueldo):

        #constructo clase padre ,para heredar
        super().__init__(nombre, edad)

        self.sueldo = sueldo




#metodo str para clase padre
    def __str__(self):

        # super (acceder a la clase padre)
        return f'Empleados :[{super().__str__()}]  Sueldo:{self.sueldo}'


