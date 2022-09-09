from Disciplina import Disciplina

class Aluno():
    
    def __init__(self, nome = "", email = "", disciplinas = [], iaa = 0):
        self.__nome = nome;
        self.__email = email;
        self.__disciplinas = disciplinas;
        self.__iaa = iaa;
        
    def getNome(self) -> str:
        return self.__nome;
        
    def getEmail(self) -> str:
        return self.__email;
    
    def getDisciplinas(self) -> list:
        return self.__disciplinas;
        
    def getIaa(self) -> float:
        return self.__iaa;
        
    def setNome(self, nome):
        self.__nome = nome;
        
    def setEmail(self, email):
        self.__email = email;
        
    def setDisciplinas(self, disciplinas):
        self.__disciplinas = disciplinas;
        
    def setIaa(self, iaa):
        self.__iaa = iaa;
        

d1 = Disciplina("INE001", "POO 2", 2);
d2 = Disciplina("INE002", "SD", 2);
d3 = Disciplina("INE003", "CTS", 2);
d4 = Disciplina("INE004", "HM", 1);

a1 = Aluno("Micael", "micael@gmicael.org", [d1, d2, d3, d4], 8);

print(a1.getNome());
print(a1.getEmail());
print(a1.getDisciplinas()[0].getNome());
print(a1.getDisciplinas()[1].getNome());
print(a1.getDisciplinas()[2].getNome());
print(a1.getDisciplinas()[3].getNome());
print(a1.getIaa());
        
        