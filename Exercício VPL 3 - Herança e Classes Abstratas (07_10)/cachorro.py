from mamifero import Mamifero

class Cachorro(Mamifero):
    def __init__(self, volumeSom=3, tamanhoPasso=3) -> None:
        super().__init__(volumeSom, tamanhoPasso)
    
    def produzir_som(self):
        return super().produzir_som() + " SOM: AU"
    
    def mover(self):
        return super().mover()
    
    def latir(self):
        return super().produzir_som() + " SOM: AU"