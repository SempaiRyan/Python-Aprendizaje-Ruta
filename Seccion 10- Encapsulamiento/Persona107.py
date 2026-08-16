class Persona():
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # Get
    @property  # recuperar nombre=_nombre a travez del metodo
    def nombre(self):
        return self._nombre

    # Set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

per1 = Persona('Juan', 'Perez', 22)
per1.nombre = 'Juan Carlos'
per1.apellido = 'Lara'
per1.edad = 30
per1.mostrarDetalle()
print(__name__)
