'''
Seja n o grau de um dado polinômio
Assumi que coeficientes nulos em variáveis de grau menor que n estão representados (i.e. 4 + 0x + 2x²)
Mantive a ordem fornecida na questão
Na hora de plotar, exigi que o intervalo fosse dado em ordem
'''

class Polinomio():
    
    def __init__(self, coeficientes = list()):
        self.__coeficientes = coeficientes;
        
    def getCoeficientes(self):
        return self.__coeficientes;
        
    def setCoeficientes(self, coeficientes):
        self.__coeficientes = coeficientes;
        
    def grau(self):
        return len(self.__coeficientes) - 1;
        
    def avaliar(self, x):
        
        sum = 0;
        for e, num in enumerate(self.__coeficientes):
            # print(f"{num}*({x}**{e}) = {num*(x**e)}"); debug, esqueci que potencia em python é ** e não ^
            sum += num*(x**e);
            
        return sum;
    
    def somarPolinomio(self, polinomio):
        
        selfLen = self.grau() + 1;
        paramLen = polinomio.grau() + 1;
        
        np = list();
        
        for k in range(max(selfLen, paramLen)):
            
            if (selfLen <= k):
                sCo = 0;
            else:
                sCo = self.__coeficientes[k];
            
            if (paramLen <= k):
                pCo = 0;
            else:
                pCo = polinomio.getCoeficientes()[k];
                
            np.append(sCo + pCo);
        
        return Polinomio(np);
        
    def multiplicarPolinomio(self, polinomio):
        
        novoGrau = self.grau() + polinomio.grau();
        
        listaPxs = list();
        
        # Achar o maior polinomio
        maiorPolinomio = polinomio;
        menorPolinomio = self;
        
        if (self.grau() > polinomio.grau()):
            maiorPolinomio = self;
            menorPolinomio = polinomio;
        
        # Montar os coeficientes para serem somados posteriormente
        for i, co in enumerate(maiorPolinomio.getCoeficientes()):
            
            nl = list();
            
            for t in range(i):  # acrescentando zeros à esquerda
                nl.append(0);   # não preciso acrescentar zeros à direita pois o somador de polinômios ja faz isso
                
            for aco in menorPolinomio.getCoeficientes():
                nl.append(co*aco);
                
            np = Polinomio(nl);
            listaPxs.append(np);
        
        # Somando os coeficientes resultantes
        k = maiorPolinomio.grau();
        pSum = Polinomio([0]*novoGrau);
        while 0 <= k:
            print(listaPxs[k].getCoeficientes());
            pSum = pSum.somarPolinomio(listaPxs[k]);
            k -= 1;
            
        return pSum;
        
    # DESAFIO WIP
    def plota(self, a, b):
        
        if (b < a):
            return None;
            
        elif (a == b):
            return self.avaliar(a);
            
        else:
            
            y = list();
            for num in range(a, b+1): # pois range é [a, b)
                y.append(self.avaliar(num));
            
            menor = min(y);
            maior = max(y);
            
            lx = len(list(range(a, b+1)));
            ly = len(list(range(menor, maior+1)));
            
            plano = list([" "]*ly);
            
            
            
            
            
                
            
            
            
                   
p = Polinomio([1, 1, 1]);
p2 = Polinomio([2, 4, 8, 6]);
p3 = Polinomio([10, 10, 10, 10, 10, 10, 10]);
print(p.avaliar(3));
px = Polinomio(p.somarPolinomio(p2));
print(px.getCoeficientes());
print(p3.somarPolinomio(p3));
print(p3.somarPolinomio(p2));
print(p2.somarPolinomio(p3));
print(p2.avaliar(5));
print(p3.grau());

pt = Polinomio([3, 2, 1]);
pt2 = Polinomio([1, 2, 3, 4]);
print(pt.multiplicarPolinomio(pt2).getCoeficientes());

print("_"*100);
