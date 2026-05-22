class Persona:
    # Su# función principal es inicializarlos
    # atributos del objeto, es decir, darle valores
    # iniciales.

    def __init__(self,nombre,apellido,edad) :

        #self es una instacia
        self._nombre=nombre
        self.apellido=apellido
        self.edad=edad



    #metodo de instancia
    def mostrar_detalles(self):
        #Atributos self.nombre
        print(f'Persona : {self._nombre},{self.apellido},{self.edad}')



# Crear un objeto
#p1 Persona1
persona1=Persona('Juan','Perez',20)
persona1._nombre='Juan Carlos'
persona1.mostrar_detalles()
