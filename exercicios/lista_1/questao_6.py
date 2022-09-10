class Carta():
    
    def __init__(self, simbolo, cor, tipo) -> None:
        self.__simbolo = simbolo;
        self.__cor = cor;
        self.__tipo = tipo;
        
class Baralho():
    
    def __init__(self, cartas = [Carta(None, None, None)]):
        self.__cartas = cartas;