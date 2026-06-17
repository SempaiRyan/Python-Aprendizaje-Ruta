
class Monitor():

    contador_monitor =0
    def __init__(self,marca,tamano):

        Monitor.contador_monitor +=1

        self._id_monitor = Monitor.contador_monitor

        self._marca = marca

        self._tamano = tamano

    def __str__(self):
        return f'ID {self._id_monitor} + Marca {self._marca} + Tamano {self._tamano}'
if __name__ == '__main__':
    monitor = Monitor('Monitor 1',15)
    print(monitor)
    monitor2 = Monitor('Monitor 2',24)
    print(monitor2)