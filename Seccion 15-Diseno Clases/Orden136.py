from Creacion135 import Producto


class Orden:
    contador_orden=0

    def __init__(self,productos):
        Orden.contador_orden=Orden.contador_orden+1
        self._id_orden=Orden.contador_orden
        self._productos=list(productos)


    def agregar_producto(self,producto):
        self._productos.append(producto)


    def calcular_total(self):
        total=0
        for producto in self._productos:
            total +=producto.precio_get

        return total


    def __str__(self):
        producto_Str=''
        for producto in self._productos:
            producto_Str +=producto.__str__()+'||||'

        return f'Orden : {self._id_orden}   \n Productos: {producto_Str}'


if __name__ == '__main__':
    producto1=Producto('Camisa 2222',1,100)
    producto2=Producto('Pantalon 2222',2,150)
    productos1=[producto1,producto2]
    orden1=Orden(productos1)
    print(orden1)