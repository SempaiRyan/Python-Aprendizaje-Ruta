class Persona():
    def __init__(self, nombre,apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad


    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')


per1=Persona('Juan','Perez',22)
per1._nombre='Juan Carlos'
per1.mostrarDetalle()