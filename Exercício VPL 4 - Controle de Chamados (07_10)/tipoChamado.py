from interfaces.abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__nome = nome
        
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def descricao(self) -> str:
        return self.__descricao
    
    @property
    def nome(self) -> str:
        return self.__nome
        
    