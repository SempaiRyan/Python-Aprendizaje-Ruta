class Persona:
    # Su# función principal es inicializarlos
    # atributos del objeto, es decir, darle valores
    # iniciales.

    def __init__(self,nombre,apellido,edad) :
        #self es un instancia
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

# Crear un objeto
#p1 Persona1
persona1=Persona('Juan','Perez',20)


print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)