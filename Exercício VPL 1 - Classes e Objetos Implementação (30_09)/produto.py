
class Produto:

    def __init__(self, codigo, descricao, categoria):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria
        self.__quantidade = 0
        self.__preco_unitario = 0
        self.__cliente = ""
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter        
    def codigo(self, newCodigo):
        self.__codigo = newCodigo
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter        
    def descricao(self, newDesc):
        self.__descricao = newDesc
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter        
    def categoria(self, newCat):
        self.__categoria = newCat
 
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter        
    def quantidade(self, newQuant):
        self.__quantidade = newQuant
 
    @property
    def preco_unitario(self):
        return self.__preco_unitario
    
    @preco.setter        
    def preco_unitario(self, newPreco):
        self.__preco_unitario = newPreco
 
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter        
    def cliente(self, newCliente):
        self.__cliente = newCliente
 
    def preco_total(self):
        return self.preco_unitario * self.quantidade
 
    
