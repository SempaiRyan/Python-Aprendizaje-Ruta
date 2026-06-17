from dispo_entrada import Dispositivo_entrada

class Teclados(Dispositivo_entrada):
    contador_teclado=0

    def __init__(self,marca,tipo_entrada):

        Teclados.contador_teclado+=1

        self._id_teclado=Teclados.contador_teclado

        super().__init__(marca,tipo_entrada)


    def __str__(self):
        return f'ID {self._id_teclado}+ Marca: {self.marca} Tipo: {self.tipo_entrada}'

if __name__=='__main__':
    teclado1=Teclados("HP TECLADO",'USB TP')
    print(teclado1)
    teclado2=Teclados("BLUUETOOH TECLA",'USB BLUEE')
    print(teclado2)