from interfaces.abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = list()
        self.__tecnicos = list()
    
    @property
    def clientes(self) -> list:
        return self.__clientes
    
    @property
    def tecnicos(self) -> list:
        return self.__tecnicos
    
    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        novoCliente = Cliente(nome, codigo)
        
        found = False
        for c in self.__clientes:
            if novoCliente.codigo == c.codigo:
                found = True
        
        if not found:
            self.clientes.append(novoCliente)
        
        return novoCliente
        
    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        novoTecnico = Tecnico(nome, codigo)
        
        found = False
        for t in self.tecnicos:
            if novoTecnico.codigo == t.codigo:
                found = True
        
        if not found:
            self.tecnicos.append(novoTecnico)
        
        return novoTecnico