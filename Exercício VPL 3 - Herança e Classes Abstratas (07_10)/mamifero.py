from abc import ABC, abstractmethod
from animal import Animal

class Mamifero(Animal, ABC): 
    
    def __init__(self, volume_som, tamanho_passo) -> None:
        self.__volume_som = volume_som
        super().__init__(tamanho_passo)
    
    @property
    def volume_som(self):
        return self.__volume_som
    
    @volume_som.setter
    def volume_som(self, volume_som):
        self.__volume_som = volume_som
    
    def mover(self):
        return super().mover()
    
    @abstractmethod
    def produzir_som(self):
        return "MAMIFERO: PRODUZ SOM: "+self.__volume_som 