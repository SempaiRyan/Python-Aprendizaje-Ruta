class Persona:
    contador_persona=0


    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona+=1
        return cls.contador_persona


    def __init__(self,nombre,edad):
        self.id_persona=Persona.generar_siguiente_valor()
        self.nombre=nombre
        self.edad=edad



    def __str__(self):
        return f'Persona : [{self.id_persona}  {self.nombre} {self.edad} ] '



persona1=Persona('Juan',29)
print(persona1)

persona2=Persona('Karla',35)
print(persona2)


persona3=Persona('Mick',68)
print(persona3)


Persona.generar_siguiente_valor()

persona4=Persona('MARIA',99)


print(f'Valor contador personas: {Persona.contador_persona}')