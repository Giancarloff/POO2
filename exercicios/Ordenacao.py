"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar: list()):
        self.array_para_ordenar = array_para_ordenar;

    def ordena(self):
        
        _a = self.array_para_ordenar;
        _len = len(_a);
        _na = list(range(_len));
        
        for num in _a:
            count = 0;
            rep = -1;
            for num2 in _a:
                if (num2 < num):
                    count += 1;
                if (num2 == num):
                    rep += 1;
            
            _na[count] = num;
            while rep > 0:
                _na[count + rep] = num;
                rep -= 1;
        
        # no máximo n² + n passos
        
        self.array_para_ordenar = _na;
        
        return self.array_para_ordenar;

    def toString(self):
        
        _str = "\"";
        
        for i in self.array_para_ordenar:
            _str = _str + format(i) + ",";
        
        
        _str = _str[0:len(_str)-1] + "\"";
        
        return _str;
    
    

print("numeros: ");
numeros_str = input().split();
numeros = list();

#print(numeros_str);

for n in numeros_str:
    numeros.append(int(n));

#print(numeros);
o = Ordenacao(numeros);

o.ordena();
print(o.toString());
"""
o = Ordenacao([9, 0, 8, 1, 7, 2, 6, 3, 5, 4]);
o2 = Ordenacao([9, 9, 8, 7, 6, 2, 1, 1]);
print(o.toString(o.ordena()));
print(o2.toString(o2.ordena()));
"""