from abc import ABC, abstractmethod


class Transporte(ABC):
    
    def __init__(self, nome, altura, comprimento, carga, velocidade) -> None:
        self._nome = nome
        self._altura = altura
        self._comprimento = comprimento
        self._carga = carga
        self._velocidade = velocidade
    
    @abstractmethod   
    def __str__(self) -> str:
        s = f"Nome: {self._nome}; Altura: {self._altura}; Comprimento: {self._comprimento}; "
        s += f"Carga: {self._carga}; Velocidade: {self._velocidade}; "
        
        return s
    
class TransporteAereo(Transporte):
    
    def __init__(self, nome, altura, comprimento, carga, velocidade, autonomia, envergadura) -> None:
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura
        
    def __str__(self) -> str:
        s = f"Nome: {self._nome}; Altura: {self._altura}; Comprimento: {self._comprimento}; "
        s += f"Carga: {self._carga}; Velocidade: {self._velocidade}; "
        s += f"Autonomia: {self.__autonomia}; Envergadura: {self.__envergadura};"
        
        return s
        
class TransporteTerrestre(Transporte):
    
    def __init__(self, nome, altura, comprimento, carga, velocidade, motor, roda) -> None:
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__roda = roda
        
    def __str__(self) -> str:
        s = f"Nome: {self._nome}; Altura: {self._altura}; Comprimento: {self._comprimento}; "
        s += f"Carga: {self._carga}; Velocidade: {self._velocidade}; "
        s += f"Motor: {self.__motor}; Roda: {self.__roda};"
        
        return s
                
class TransporteAquatico(Transporte):
    
    def __init__(self, nome, altura, comprimento, carga, velocidade, boca, calado) -> None:
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    def __str__(self) -> str:
        s = f"Nome: {self._nome}; Altura: {self._altura}; Comprimento: {self._comprimento}; "
        s += f"Carga: {self._carga}; Velocidade: {self._velocidade}; "
        s += f"Boca: {self.__boca}; Calado: {self.__calado};"
        
        return s
    
class Catalogo:
    
    def __init__(self) -> None:
        self.__transportesAereos = list()
        self.__transportesTerrestres = list()
        self.__transportesAquaticos = list()
    
    @property
    def transportesAereos(self) -> list:
        return self.__transportesAereos
        
    @property
    def transportesTerrestres(self) -> list:
        return self.__transportesTerrestres
    
    @property
    def transportesAquaticos(self) -> list:
        return self.__transportesAquaticos
    
    def novoTransporte(self, nta: Transporte):
        
        if (isinstance(nta, TransporteAereo)):
            self.transportesAereos.append(nta)
        
        elif (isinstance(nta, TransporteAquatico)):
            self.transportesAquaticos.append(nta)
        
        elif (isinstance(nta, TransporteTerrestre)):
            self.transportesTerrestres.append(nta)
        
        else:
            return None
    
    def mostrarTransportes(self):
        print("Aéreos: ")
        for a in self.transportesAereos:
            print(a)
        
        print("Terrestres: ")
        for t in self.transportesTerrestres:
            print(t)
            
        print("Aquáticos: ")
        for aq in self.transportesAquaticos:
            print(aq)
            
a1 = TransporteAereo("a1", 10, 10, 10, 10, 10, 10)
a2 = TransporteAereo("a2", 20, 20, 20, 20, 20, 20)

t1 = TransporteTerrestre("t1", 10, 10, 10, 10, 10, 10)
t2 = TransporteTerrestre("t2", 20, 20, 20, 20, 20, 20)

aq1 = TransporteAquatico("aq1", 10, 10, 10, 10, 10, 10)
aq2 = TransporteAquatico("aq2", 20, 20, 20, 20, 20, 20)

cat = Catalogo()
cat.novoTransporte(a1)
cat.novoTransporte(a2)
cat.novoTransporte(t1)
cat.novoTransporte(t2)
cat.novoTransporte(aq1)
cat.novoTransporte(aq2)
cat.mostrarTransportes()

