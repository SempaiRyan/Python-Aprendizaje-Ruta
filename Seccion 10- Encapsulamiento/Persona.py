# 105. Métodos Get y Set en Python
"""
GET OBTENER/RECUPERAR
SET=COLOCAR /MODIFICAR

"""
class Persona:

    def __init__(self,nombre,apellido,edad) :

        #self es una instacia
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad


    #decorador acceder al metodo nombre
    @property
    def nombre(self):

        return self._nombre

    #Metodo set
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        return self._apellido


    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
        self._edad=edad

    #metodo de instancia
    def mostrar_detalles(self):
        #Atributos self.nombre
        print(f'Persona : {self._nombre},{self._apellido},{self._edad}')


if __name__=='name':

# Crear un objeto
    persona1=Persona('Juan','Perez',20)
    persona1.nombre=('Juan Carlos')

    persona1.apellido=('Lara')
    persona1.edad=230
    persona1.mostrar_detalles()

# persona1.nombre=('Cambio')
# print(persona1.nombre)


    print(__name__)