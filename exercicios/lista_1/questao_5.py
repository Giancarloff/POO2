'''
Assumi permutação, arranjo e combinação simples

P = n!

A = n!/(n-k)!

C = n!/r!(n-r)!

'''

class Fatorial():
    
    def __init__(self, x) -> None:
        return self.get(x);
    
    def get(self, x):
        
        if (x == 1 or x == 0):
            return 1;
            
        return x*self.get(x-1);
    
    def upto(self, x):
        
        tr = list();
        for i in list(range(x)):
            tr.append(self.get(i));
            
        return tr;
        
class Fracao():
    

