# 105. Métodos Get y Set en Python
"""
GET OBTENER/RECUPERAR
SET=COLOCAR /MODIFICAR

"""
class Persona:

    def __init__(self,nombre,apellido,edad) :

        #self es una instacia
        self._nombre=nombre
        self.apellido=apellido
        self.edad=edad


    #decorador acceder al metodo nombre
    @property
    def nombre(self):
        print('Llamando metodo get nombre')

        return self._nombre


    #Metodo set
    @nombre.setter
    def nombre(self,nombre):
        print('Llamando metodo set nombre')
        self._nombre=nombre

    #metodo de instancia
    def mostrar_detalles(self):
        #Atributos self.nombre
        print(f'Persona : {self._nombre},{self.apellido},{self.edad}')



# Crear un objeto
#p1 Persona1
persona1=Persona('Juan','Perez',20)
persona1._nombre='Juan Carlos'
persona1.mostrar_detalles()

#Atributo al metodo nombre (ya no se pone parentesis)
persona1.nombre=('Juan Carlos')
print(persona1._nombre)


# persona1.nombre=('Cambio')
# print(persona1.nombre)