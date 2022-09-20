from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException

class Elevador(AbstractElevador):
    
    def __init__(self, andarAtual, totalAndaresPredio, capacidade, totalPessoas):
        self.__andarAtual= andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas
        
        
    def descer(self) -> str:
        self.__andarAtual -= 1
        return "Elevador.descer()"
        
    def entraPessoa(self) -> str:
        self.__totalPessoas += 1
        return "Elevador.entraPessoa()"
        
    def saiPessoa(self) -> str:
        self.__totalPessoas -= 1
        return "Elevador.saiPessoa()"
        
    def subir(self) -> str:
        self.__andarAtual += 1
        return "Elevador.subir()"
        
    @property
    def capacidade(self) -> int:
        return self.__capacidade
        
    @property
    def totalPessoas(self) -> int:
        return self.__totalPessoas
        
    @property
    def totalAndaresPredio(self) -> int:
        return self.__totalAndaresPredio
    
    @property
    def andarAtual(self) -> int:
        return self.__andarAtual
    
    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int) -> int:
        self.__totalAndaresPredio = totalAndaresPredio
        