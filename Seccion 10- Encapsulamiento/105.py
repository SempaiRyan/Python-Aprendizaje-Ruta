class Persona():
    def __init__(self, nombre,apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #Get
    @property #recuperar nombre=_nombre a travez del metodo
    def nombre(self):
        print('Llamando get')
        return self._nombre

    #Set
    @nombre.setter
    def nombre(self,nombre):
        print('Llamando set')
        self._nombre = nombre


    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')


per1=Persona('Juan','Perez',22)
per1.nombre='Juan Carlos'
print(per1.nombre)

