from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevador import Elevador
from elevadorJahVazioException import ElevadorJahVazioException

class ControladorElevador(AbstractControladorElevador):

    def __init__(self):
        super().__init__()

    def subir(self) -> str:
        if self.elevador.andarAtual == self.elevador.totalAndaresPredio - 1:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.elevador.subir()
            return "ControladorElevador.subir()"

    def descer(self) -> str:
        if self.elevador.andarAtual - 1 < 0:
            raise ElevadorJahNoTerreoException
        else:
            self.elevador.descer()
            return "ControladorElevador.descer()"

    def entraPessoa(self) -> str:
        if self.elevador.totalPessoas + 1 > self.elevador.capacidade:
            raise ElevadorCheioException
        else:
            self.elevador.entraPessoa()
            return "ControladorElevador.entraPessoa()"

    def saiPessoa(self) -> str:
        if self.elevador.totalPessoas - 1 < 0:
            raise ElevadorJahVazioException
        else:
            self.elevador.saiPessoa()
            return "ControladorElevador.saiPessoa()"

    @property
    def elevador(self) -> Elevador:
        return self.__elevador
    
    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        
        parametrosInteiros = (
            isinstance(andarAtual, int) and
            isinstance(totalAndaresPredio, int) and
            isinstance(capacidade, int) and
            isinstance(totalPessoas, int)
        )
    
        todosPositivos = False
        atendeLimites = False
        if parametrosInteiros:
            todosPositivos = not (
                andarAtual < 0 or
                totalAndaresPredio < 0 or
                capacidade < 0 or
                totalPessoas < 0
            )
                        
            atendeLimites = (
                andarAtual < totalAndaresPredio and
                totalPessoas <= capacidade
            )

        
        parametrosValidos = (parametrosInteiros and todosPositivos and atendeLimites)
        
        if parametrosValidos:
            self.__elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)
        else:
            raise ComandoInvalidoException
            