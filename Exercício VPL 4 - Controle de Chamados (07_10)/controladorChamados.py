from interfaces.abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self) -> None:
        self.__chamados = list()
        self.__tiposChamados = list()
        
    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        r = 0
        for c in self.__chamados:
            if c.tipo == tipo:
                r += 1
        
        return r    
    
    def incluiChamado(
        self, 
        data: Date, 
        cliente: Cliente, 
        tecnico: Tecnico, 
        titulo: str, 
        descricao: str, 
        prioridade: int, 
        tipo: TipoChamado) -> Chamado:
        
        novoChamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
        
        found = False
        for ch in self.__chamados:
            
            teste = (
                novoChamado.data == ch.data and
                novoChamado.cliente == ch.cliente and
                novoChamado.tecnico == ch.tecnico and
                novoChamado.tipo == ch.tipo 
            )
                
            if teste:
                found = True
        
        if not found:
            self.tipoChamados.append(novoChamado)
        
        return novoChamado
        
    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        tipoChamado = TipoChamado(codigo, descricao, nome)
        
        found = False
        for tc in self.tipoChamados:
            if tipoChamado.codigo == tc.codigo:
                found = True
        
        if not found:
            self.tipoChamados.append(tipoChamado)
        
        return tipoChamado
    
    @property
    def tipoChamados(self):
        return self.__tiposChamados
