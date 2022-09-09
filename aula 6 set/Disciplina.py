class Disciplina():
    
    def __init__(self, codigo = "", nome = "", numTurmas = 0):
        self.__codigo = codigo;
        self.__nome = nome;
        self.__numTurmas = numTurmas;
    
    def getCodigo(self) -> int:
        return self.__codigo;
        
    def getNome(self) -> str:
        return self.__nome;
    
    def getNumTurmas(self) -> int:
        return self.__numTurmas;
    
    def setCodigo(self, codigo):
        self.__codigo = codigo;
    
    def setNome(self, nome):
        self.__nome = nome;
    
    def setNumTurmas(self, numTurmas):
        self.__numTurmas: numTurmas;
        
    