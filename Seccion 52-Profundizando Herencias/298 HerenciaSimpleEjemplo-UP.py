# Ejemplo de herencia simple
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'


# Lista ordenada (herencia simple)
class ListaOrdenadas(ListaSimple):
    def __init__(self, elementos=None):
        if elementos is None:
            elementos = []
        super().__init__(elementos)
        # Ordena siempre los elementos al inicializar
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordena cada vez que se agrega un nuevo elemento
        self.ordenar()


# Lista que solo acepta enteros
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=None):
        if elementos is None:
            elementos = []
        # Validar cada elemento antes de inicializar
        for e in elementos:
            self._validar(e)
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validar si es tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f"No es valor entero: {elemento}")

    # Sobreescribimos el método agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)


#301 HERENCIA MULTIPLE



# Pruebas
lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)

lista_ordenadas = ListaOrdenadas([4, 3, 6, 9, 10, -11])
print(lista_ordenadas)

lista_ordenadas.agregar(-14)
print(lista_ordenadas)
print(len(lista_ordenadas))

lista_enteros = ListaEnteros([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(lista_enteros)
