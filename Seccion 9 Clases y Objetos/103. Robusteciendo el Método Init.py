class Persona:
    # Su# función principal es inicializarlos
    # atributos del objeto, es decir, darle valores
    # iniciales.

    def __init__(self,nombre,apellido,edad,*valores,**terminos) :
        #self es un instancia
        #valores = tuplas
        #terminos=diccionarios datos
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad


        self.valores=valores
        self.terminos=terminos

    #metodo de instancia
    def mostrar_detalles(self):

        #Atributos self.nombre
        print(f'Persona : {self.nombre},{self.apellido},{self.edad} ,{self.valores},{self.terminos}')



# Crear un objeto
#p1 Persona1
persona1=Persona('Juan','Perez',20,'44553322',2,3,5,m='Manzana',p='Pera')
persona1.mostrar_detalles()


persona2=Persona('Karla','Gomez',30)
persona2.mostrar_detalles()