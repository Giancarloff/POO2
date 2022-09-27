from abc import ABC, abstractmethod
from interfaces.abstractPessoa import AbstractPessoa

class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        self._nome = nome
        self._codigo = codigo
        
    @property
    @abstractmethod
    def nome(self) -> str:
        return self._nome
    
    @property
    @abstractmethod
    def codigo(self) -> int:
        return self._codigo