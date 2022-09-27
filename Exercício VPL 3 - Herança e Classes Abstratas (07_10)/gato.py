from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self, volume_som=2, tamanho_passo=2) -> None:
        super().__init__(volume_som, tamanho_passo)
    
    def produzir_som(self):
        return super().produzir_som() + " SOM: MIAU"
    
    def mover(self):
        return super().mover()
    
    def miar(self):
        return super().produzir_som() + " SOM: MIAU"