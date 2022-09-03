import numpy as np
from Nodo import Nodo

class ListaPorCursor:
    __arreglo:np.ndarray
    __cabeza:int
    __cabezaLibre:int
    __cantidad:int

    def __init__(self, dimension=5, tipo:type=int) -> None:
        self.__arreglo = np.empty(dimension, dtype=Nodo)
        self.__cabeza = -1
        self.__cabezaLibre = 0
        self.__cantidad = 0
        for i in range(dimension-1):
            unNodo = Nodo(None)
            unNodo.setSig(i+1)
            self.__arreglo[i] = unNodo
        self.__arreglo[dimension-1] = -1
    
    def vacia(self):
        return self.__cabeza == -1

    def insertar(self, elemento, posicion: int):
        if self.__cabezaLibre == -1:
            raise OverflowError("La lista está llena")
        if posicion < 1:
            raise Exception("La posicion debe ser mayor a 1")
        if posicion > self.__cantidad + 1:
            raise Exception("No se puede insertar en la posicion {0}, la lista solo tiene {1} elementos".format(posicion, self.__cantidad))
        
        unNodo = Nodo(elemento)

        ubicacion_nuevo = self.__cabezaLibre
        self.__cabezaLibre = self.__arreglo[self.__cabezaLibre].getSig()
        self.__arreglo[ubicacion_nuevo] = unNodo

        if posicion == 1:
            unNodo.setSig(self.__cabeza)
            self.__cabeza = ubicacion_nuevo

        else:
            anterior = -1
            unNodo.setSig(self.__cabeza)
            for i in range(posicion-1):
                anterior = unNodo.getSig()
                unNodo.setSig(self.__arreglo[unNodo.getSig()].getSig())
            self.__arreglo[anterior].setSig(ubicacion_nuevo)
        
        self.__cantidad += 1
    
    def suprimir(self, posicion: int):
        if self.vacia():
            raise Exception("No hay elementos en la lista")
        if posicion < 1:
            raise Exception("La posicion debe ser mayor o igual a 1")
        if posicion > self.__cantidad:
            raise Exception("No se puede suprimir un elemento en la posicion {0}, la lista solo tiene {1} elementos".format(posicion, self.__cantidad))
        
        if posicion == 1:
            elemento = self.__arreglo[self.__cabeza].getElemento()
            posicion_liberada = self.__cabeza
            self.__cabeza = self.__arreglo[self.__cabeza].getSig()
            self.__arreglo[posicion_liberada].setSig(self.__cabezaLibre)
            self.__cabezaLibre = posicion_liberada
        else:
            liberada = self.__cabeza
            anterior = -1
            for i in range(posicion - 1):
                anterior = liberada
                liberada = self.__arreglo[liberada].getSig()
            elemento = self.__arreglo[liberada].getElemento()
            self.__arreglo[anterior].setSig(self.__arreglo[liberada].getSig())
            self.__arreglo[liberada].setSig(self.__cabezaLibre)
            self.__cabezaLibre = liberada
        
        self.__cantidad -= 1
        return elemento
    

    def recuperar(self, posicion: int):
        if self.vacia():
            raise Exception("La lista está vacía")
        if posicion < 1:
            raise Exception("La posición debe ser mayor a 1")
        if posicion > self.__cantidad:
            raise Exception("No se puede recuperar un elemento en la posición {0}, la lista solo tiene {1} elementos".format(posicion, self.__cantidad))
        
        if posicion == 1:
            elemento = self.__arreglo[self.__cabeza].getElemento()
        
        else:
            actual = self.__cabeza
            for i in range(posicion-1):
                actual = self.__arreglo[actual].getSig()
            elemento = self.__arreglo[actual].getElemento()
        
        return elemento


    
    def recorrer(self, operacion):
        actual = self.__cabeza
        for i in range(self.__cantidad):
            operacion(self.__arreglo[actual].getElemento())
            actual = self.__arreglo[actual].getSig()
    
    def primer_elemento(self):
        return self.__arreglo[self.__cabeza].getElemento()
    
    def ultimo_elemento(self):
        return self.recuperar(self.__cantidad)
    
    def siguiente(self, posicion):
        return self.recuperar(posicion+1)
    
    def anterior(self, posicion):
        return self.recuperar(posicion-1)