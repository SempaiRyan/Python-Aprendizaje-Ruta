class Persona:
    def __init__(self, nombre,edad):

        self.nombre = nombre
        self.edad = edad


    #Metodo operador suma
    def __add__(self, other):
        return f' {self.nombre} + {other.nombre} '

    def __sub__(self, other):
        return   {self.edad}-{other.edad}

per1=Persona("Juan",28)
per2=Persona("Carlitos",40)

#Concatenacion
print(per1+per2)
print(per1-per2)

