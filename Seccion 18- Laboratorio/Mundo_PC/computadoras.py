from teclado import Teclados
from raton import Raton
from monitor import Monitor


class Computadoras():
    contador_computador = 0

    def __init__(self,nombre,monitor,teclado,raton):
        Computadoras.contador_computador +=1
        self._id_computador=Computadoras.contador_computador

        self._nombre=nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton


    def __str__(self):
        return f''''
        Monitor : {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        
         
        '''
tecla1=Teclados('RYZEN','USB RYZEN')

raton1=Raton('INTEL','BLUTOOH')

monitor1=Monitor('Intelestelar',25)


compu1=Computadoras('HP',monitor1,tecla1,raton1)
print(compu1)