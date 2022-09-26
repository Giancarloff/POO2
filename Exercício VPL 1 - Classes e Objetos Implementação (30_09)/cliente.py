class Cliente:
    
    def __init__(self, nome, fone) -> None:
        self.__nome = nome
        self.__fone = fone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, newNome):
        self.__nome = newNome
        
    @property
    def fone(self):
        return self.__fone
        
    @fone.setter
    def fone(self, newFone):
        self.__fone = newFone
        
    
