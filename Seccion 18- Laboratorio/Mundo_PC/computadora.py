from dispo_entrada import Dispositivo_Entrada
from teclado import Teclado
from monitor import Monitor
from raton import Raton

class Computadora():
    contador_computadora=0

    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadora+=1

        self._id_computadora=Computadora.contador_computadora

        self._nombre=nombre

        self._monitor=monitor

        self._teclado=teclado

        self._raton=raton

    def __str__(self):
        return f'''
        ID: {self._id_computadora}
        Nombre: {self._nombre}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

if __name__=='__main__':
    teclado1=Teclado('HP','USB')
    raton1=Raton('INTEL','PILA')
    monitor1=Monitor('HP',15)
    compu1=Computadora('HP INTEL 9NA',monitor1,teclado1,raton1)
    print(compu1)


    teclado2 = Teclado('Logitech', 'Bluetooth')
    raton2 = Raton('Razer', 'USB-C')
    monitor2 = Monitor('Samsung', 27)
    compu2 = Computadora('Acer Nitro Ryzen 7', monitor2, teclado2, raton2)
    print(compu2)