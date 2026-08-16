from teclado import Teclado
from raton import Raton
from monitor import Monitor
from computadora import Computadora
from ordenes import Orden


teclado1 = Teclado('HP', 'USB')
raton1 = Raton('INTEL', 'PILA')
monitor1 = Monitor('HP', 15)
computadora1 = Computadora('HP INTEL 9NA', monitor1, teclado1, raton1)
print(computadora1)

teclado2 = Teclado('Logitech', 'Bluetooth')
raton2 = Raton('Razer', 'USB-C')
monitor2 = Monitor('Samsung', 27)
computadora2 = Computadora('Acer Nitro Ryzen 7', monitor2, teclado2, raton2)
print(computadora2)



teclado3 = Teclado('Corsair', 'USB')
raton3 = Raton('SteelSeries', 'Inalámbrico')
monitor3 = Monitor('LG', 32)
computadora3 = Computadora('Gamer MSI Raider i9', monitor3, teclado3, raton3)




#Lista de objeto computadoras


computadoras1=[computadora1,computadora2]
orden1=Orden(computadoras1)
# print(orden1)

orden1.agregar_Computadora(computadora3)
print(orden1)

computadoras2=[computadora2,computadora3]
orden2=Orden(computadoras2)
print(orden2)