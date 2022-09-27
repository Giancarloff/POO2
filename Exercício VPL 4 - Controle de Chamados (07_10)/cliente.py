from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
    
    @property
    def nome(self) -> str:
        return super().nome
    
    @property
    def codigo(self) -> int:
        return super().codigo