from ave import Ave

class Canarinho(Ave):
    
    def __init__(self, tamanho_passo, altura_voo) -> None:
        super().__init__(tamanho_passo, altura_voo)
    
    def mover(self):
        return super().mover()
        
    def cantar(self):
        return super().produzirSom()