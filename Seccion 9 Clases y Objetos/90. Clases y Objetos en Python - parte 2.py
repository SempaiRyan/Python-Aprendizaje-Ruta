class Persona:
    # Su# función principal es inicializarlos
    # atributos del objeto, es decir, darle valores
    # iniciales.

    def __init__(self) :
        #self es un instancia
        self.nombre='Juan'
        self.apellido='Perez'
        self.edad=28

# Crear un objeto
#p1 Persona1
persona1=Persona()


print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)