from dispo_entrada import Dispositivo_Entrada

class Raton(Dispositivo_Entrada):

    contador_raton =0

    def __init__(self,marca,tipo_entrada):

        Raton.contador_raton +=1

        self._idraton=Raton.contador_raton

        super().__init__(marca,tipo_entrada)


    def __str__(self):
        return f'ID : {self._idraton} + Marca : {self._marca}+ Tipo Entrada: {self._tipo_entrada}'



if __name__=='__main__':
    raton1=Raton('Raton HP','USB RATON')
    print(raton1)

    raton2=Raton('Raton Acer 22 HP','BLUTU 222 RATON')
    print(raton2)