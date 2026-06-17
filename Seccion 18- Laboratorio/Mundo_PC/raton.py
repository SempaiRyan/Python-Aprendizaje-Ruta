from dispo_entrada import Dispositivo_entrada

class Raton(Dispositivo_entrada):
    contador_raton=0

    def __init__(self,marca,tipo_entrada):
        Raton.contador_raton+=1
        self._idraton=Raton.contador_raton


        #Atributos heredados padre
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return f"Raton: {self._idraton}, Marca : {self._marca} ,Tipo Entrada: {self._tipo_entrada}"



if __name__=='__main__':
    raton1=Raton("HP","USB TIPO C")
    print(raton1)

    raton2=Raton("ACER","BLUEE TOOH")
    print(raton2)