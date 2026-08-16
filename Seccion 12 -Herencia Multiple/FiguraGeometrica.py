#ABC=Atract Base Class
# 125. Clases Abstractas en Python
from abc import ABC,abstractmethod



class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):


        #validacion
        if self._validarValor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor incorrecto, {ancho}')


        if self._validarValor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor incorrecto, {alto}')




    #Metodo Get y set ancho
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        if self._validarValor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor incorrecto, {ancho}')
            self._ancho = ancho



    #Metodo Get y Set de alto
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self,alto):
        if self._validarValor(alto):
            self._alto = alto
        else:
            print(f'Valor incorrecto, {alto}')


    #METODO ABSTRACT
    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'Figura Geometrica [Ancho : {self._ancho}, Alto: {self._alto}]'


    # 124. Validaciones Aplicación de Figura Geométrica - parte 2
    def _validarValor(self,valor):
        return True if 0<valor<10 else False
