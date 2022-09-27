from enum import auto
from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__autores = list()
        self.__capitulos = list()
        
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores.append(autor)
        self.__capitulos.append(Capitulo(numeroCapitulo, tituloCapitulo))

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo
        
    @property
    def ano(self):
        return self.__ano
        
    @property
    def editora(self):
        return self.__editora
        
    @property
    def autores(self):
        return self.__autores
        
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
        
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    def incluirAutor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.__autores:
            self.__autores.append(autor)

    def excluirAutor(self, autor: Autor):
        if isinstance(autor, Autor) and autor in self.autores:
            self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        tempCap = Capitulo(numeroCapitulo, tituloCapitulo)
        
        found = False
        for c in self.__capitulos:
            if tempCap.titulo == c.titulo:
                found = True
                break
        
        if not found:
            self.__capitulos.append(tempCap)

    def excluirCapitulo(self, tituloCapitulo: str):
        for i, c in enumerate(self.__capitulos):
            if c.titulo == tituloCapitulo:
                self.__capitulos.pop(i)

    def findCapituloByTitulo(self, tituloCapitulo: str) -> Capitulo:
        for c in self.__capitulos:
            if c.titulo == tituloCapitulo:
                return c

