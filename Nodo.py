class Nodo:
    __elemento = None
    __sig:int

    def __init__(self, elemento) -> None:
        self.__elemento = elemento
        self.__sig = -1
        
    def setSig(self, sig:int):
        self.__sig = sig
    
    def getSig(self) -> int:
        return self.__sig
    
    def setElemento(self, elemento):
        self.__elemento = elemento
    
    def getElemento(self):
        return self.__elemento