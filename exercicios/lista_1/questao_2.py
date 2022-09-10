class Livro():
    
    def __init__(self, titulo = "", autores = list(), ano = 0, editora = "", edicao = 0, volume = 0):
        self.__titulo = titulo;
        self.__autores = autores;
        self.__ano = ano;
        self.__editora = editora;
        self.__edicao = edicao;
        self.__volume = volume;
    
    def getTitulo(self):
        return self.__titulo;
        
    def getAutores(self):
        return self.__autores;
        
    def getAno(self):
        return self.__ano;
        
    def getEditora(self):
        return self.__editora;
        
    def getEdicao(self):
        return self.__edicao;
    
    def getVolume(self):
        return self.__volume;
        
    def setTitulo(self, titulo):
        self.__titulo = titulo;
        
    def setAutores(self, autores):
        self.__autores = autores;
    
    def setAno(self, ano):
        self.__ano = ano;
        
    def setEditora(self, editora):
        self.__editora = editora;
    
    def setEdicao(self, edicao):
        self.__edicao = edicao;
    
    def setVolume(self, volume):
        self.__volume = volume;
        
class Biblioteca():
    
    def __init__(self, livros = list()):
        self.__livros = livros;

    def pesquisar(self, term):
        pass;

    
    
    
    
    
    
    