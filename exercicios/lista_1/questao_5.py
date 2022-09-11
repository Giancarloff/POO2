'''
Assumi permutação, arranjo e combinação simples
Assumi que o usuário sempre fornecerá p < n

P = n!

A = n!/(n-p)!

C = n!/p!(n-p)!

A classe fração é uma fração mas não em sua forma mais trivial

'''

from random import randint


class Fatorial():
    
    def __init__(self, x = None) -> None:
        return self.get(x);
    
    @classmethod
    def get(self, x):
        
        if (x == 1 or x == 0):
            return 1;
            
        return x*self.get(x-1);
    
    @classmethod
    def upto(self, x):
        
        tr = list();
        for i in list(range(x)):
            tr.append(self.get(i));
            
        return tr;
    
    @classmethod
    def fatores(self, x):
        
        tr = list();
        while 0 < x:
            tr.append(x);
            x -= 1;
            
        return tr;
        
class Fracao():
    
    def __init__(self, fatoresNum: list, fatoresDen: list) -> None:
        self.__numerador = fatoresNum;
        self.__denominador = fatoresDen;
        
        if self.__denominador == []:
            self.__denominador = [1];
        
    def getNumeradores(self):
        return self.__numerador;
        
    def getDenominadores(self):
        return self.__denominador;
    
    # Esta aqui seria a otimização para reduzir cargas computacionais
    def simplificar(self):
    
        tmp = list();
        
        returnNum = list(self.__numerador);
        returnDen = list(self.__denominador);
        
        for num in returnDen:
            if (num in returnNum):
                tmp.append(num);
                returnNum.remove(num);
        
        for num2 in tmp:
            if (num2 in returnDen):
                returnDen.remove(num2);
        
        return Fracao(returnNum, returnDen);
    
class Combinacao():
    
    PERMUTACAO = 0;
    ARRANJO = 1;
    COMBINACAO = 2;
    
    def __init__(self, elementos: list, p = 0) -> None:
        self.__elementos = elementos;
        self.__p = p;
        self.__n = len(self.__elementos);
        
        if (p == 0):
            self.__p = self.__n - 1;
            
    
    def calcular(self, tipo):
        
        fatoresN = Fatorial.fatores(self.__n);
        fatoresP = Fatorial.fatores(self.__p);
        fatoresNmenosP = Fatorial.fatores(self.__n - self.__p);
        
        if (tipo == self.PERMUTACAO):
            
            nc = Fatorial.get(self.__n);
            
            ex = list();
            while len(ex) != self.__n:
                index = randint(0, self.__n - 1);
                elt = self.__elementos[index];
                if not(elt in ex):
                    ex.append(elt);
            
            print(f"EX: {ex}");
            
            return nc;
        
        elif (tipo == self.ARRANJO):
            
            nc = Fracao(fatoresN, fatoresNmenosP).simplificar();
            
            prod = 1;
            for k in nc.getNumeradores():
                prod = prod * k;
                
            # Se todo o código estiver correto, nunca deveria acontecer de div != 1
            div = 1;
            for j in nc.getDenominadores():
                div = div * j;
                
            ex = list();
            while len(ex) != self.__p:
                index = randint(0, self.__n - 1);
                elt = self.__elementos[index];
                if not(elt in ex):
                    ex.append(elt);
            
            print(f"EX: {ex}");
            
            return int(prod/div);
            
        elif (tipo == self.COMBINACAO):
            
            fatoresD = list(fatoresP);
            fatoresD.extend(fatoresNmenosP);
            nc = Fracao(fatoresN, fatoresD).simplificar();
            
            prod = 1;
            for k in nc.getNumeradores():
                prod = prod * k;
                
            div = 1;
            for j in nc.getDenominadores():
                div = div * j;
            
            ex = list();
            while len(ex) != self.__p:
                index = randint(0, self.__n - 1);
                elt = self.__elementos[index];
                if not(elt in ex):
                    ex.append(elt);
            
            print(f"EX: {ex}");
            
            return int(prod/div);
        
        else:
            
            print("Tipo inválido.");
            return None;
            
            

def main():
    
    c1 = Combinacao(['a', 'b', 'c', 'd', 'e', 'f'], 3);
    
    print(c1.calcular(c1.PERMUTACAO));
    print(c1.calcular(c1.ARRANJO));
    print(c1.calcular(c1.COMBINACAO));
    
    
    
main();

