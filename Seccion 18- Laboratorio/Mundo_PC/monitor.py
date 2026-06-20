
class Monitor():
    contador_monitor=0

    def __init__(self, marca,tamano):
        Monitor.contador_monitor+=1

        self._id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamano = tamano

    def __str__(self):
        return f'ID {self._id_monitor} | Marca : {self._marca} |Tamano {self._tamano}'


if __name__=='__main__':
    monitor1=Monitor('Monitor HP Pro',15)
    print(monitor1)

    monitor2=Monitor('Monitor Acer normal',27)
    print(monitor2)