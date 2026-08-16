class Persona:
    # Su# función principal es inicializarlos
    # atributos del objeto, es decir, darle valores
    # iniciales.

    def __init__(self,nombre,apellido,edad) :
        #self es un instancia
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

# Crear un objeto
#p1 Persona1
persona1=Persona('Juan','Perez',20)
print(f'Objeto persona 1 ,{persona1.nombre}, {persona1.apellido} ,{persona1.edad}')

# 94. Modificar Atributos de un Objeto
persona1.nombre='Juan Carlos'
persona1.apellido='Reyes'
persona1.edad=26
print(f'Objeto update ,{persona1.nombre}, {persona1.apellido} ,{persona1.edad}')




persona2=Persona('Maria','Pedro',30)
print(f'Objeto persona 2 ,{persona2.nombre}, {persona2.apellido} ,{persona2.edad}')



# 94. Modificar Atributos de un Objeto
persona2.nombre='Arianna'
persona2.apellido='Moreira'
persona2.edad=30



print(f'Objeto  update ,{persona2.nombre}, {persona2.apellido} ,{persona2.edad}')

