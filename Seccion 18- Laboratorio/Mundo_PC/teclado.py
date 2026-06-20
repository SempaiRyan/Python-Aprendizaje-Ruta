from dispo_entrada import Dispositivo_Entrada

class Teclado(Dispositivo_Entrada):
    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self._idTeclado = Teclado.contador_teclado

        # Llamada correcta al constructor de la clase padre
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID {self._idTeclado} + Marca {self._marca} + Tipo Entrada = {self._tipo_entrada}'


if __name__ == '__main__':
    teclado1 = Teclado('Teclado Max HP', 'USB')
    print(teclado1)

    teclado2 = Teclado('Teclado Max 2 Acer', 'Teclado Cable')
    print(teclado2)
