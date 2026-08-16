# Profundizar python

#dar formato en str

nombre = 'Juan Junco'
edad=28

mensaje_formato='Mi nombre es %s y tengo %d years ' %(nombre,edad)
# print(mensaje_formato)

per1=('Karla','Gomnez',5000.00)
# mensaje_formato='Hola %s %s. tu sueldo es %.2f'%per1
# print(mensaje_formato )

mensaje_formato='Hola %s %s. tu sueldo es %.2f'
print(mensaje_formato % per1)