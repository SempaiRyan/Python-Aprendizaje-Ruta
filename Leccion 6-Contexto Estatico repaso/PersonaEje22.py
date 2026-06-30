class Persona:

    contador_personas=0

    @classmethod
    def generarvalor(cls):
        #incrementar 1
        cls.contador_personas += 1
        return cls.contador_personas


    def __init__(self,nombre,edad):

        self.id_persona=Persona.generarvalor()

        self.nombre_persona=nombre

        self.edad_persona=edad

    def __str__(self):
        return f'Id Persona {self.id_persona},Nombre : {self.nombre_persona} ,Edad:  {self.edad_persona}'

per1=Persona('Juan',28)
print(per1)

per2=Persona('Karla',30)
print(per2)


per3=Persona('Carlita',22)
print(per3)


Persona.generarvalor()
per4=Persona('Maria',35)
print(per4)

print(f'Valor contador persona: {Persona.contador_personas}')







