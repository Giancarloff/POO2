class ElevadorJahVazioException(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__("O elevador já está vazio")
        