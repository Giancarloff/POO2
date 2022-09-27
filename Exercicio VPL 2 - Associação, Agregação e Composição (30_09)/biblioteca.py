from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        if isinstance(livro, Livro) and livro not in self.livros:
            self.__livros.append(livro)

    def excluirLivro(self, livro: Livro):
        check = isinstance(livro, Livro) and livro in self.__livros
        
        if check:
            self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros
