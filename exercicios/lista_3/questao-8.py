from random import randint
newline = "\n"

class MatrizEsparsa():
    
    def __init__(self) -> None:
        self.__matriz = list()
    
    def getMatriz(self):
        return self.__matriz
    
    def setMatriz(self, newMatriz = list()):
        self.__matriz = newMatriz
    
    def initTuplaDict(self, lxc = (1, 1), aij = {(0,0) : 0} ):
        nMatriz = list()
        for l in range(lxc[0]):
            linha = list()
            for c in range(lxc[1]):
                linha.append(aij.get((l, c)))
            nMatriz.append(linha)
        self.setMatriz(nMatriz)
            
    def initString(self, matrizString = "0"):

        linhasStr = matrizString.splitlines()
        for l in linhasStr:
            linha = list()
            for n in l.split():
                linha.append(int(n))
            self.__matriz.append(linha)
    
    def getAsStr(self):
        
        ls = "\""
        for l in self.__matriz:
            cs = ""
            for c in l:
                cs += str(c) + " "
            ls += cs + newline
        
        return ls[:len(ls)-2] + "\""
        
    def getAsDict(self):
        
        dmatriz = dict()
        for i, l in enumerate(self.__matriz):
            for j, c in enumerate(l):
                key = (i, j)
                dmatriz[key] = self.__matriz[i][j]
                
        return dmatriz
    
    def __str__(self) -> str:
        sr = ""
        for k in self.__matriz:
            sr += str(k) + newline
        
        return sr[:len(sr)-1] # tirando o ultimo newline
    
    
lc = (4, 9)
ij = dict()
m = 0
for k in range(4):
    for l in range(9):
        ij[(k, l)] = m % 7
        m += 1

matrizSTR = '''0 8 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 2 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 7 0 0 0 0 0
0 0 0 0 0 0 4 0 0'''

me = MatrizEsparsa()
me.initTuplaDict(lc, ij)
me2 = MatrizEsparsa()
me2.initString(matrizSTR)
print(me.getAsStr())
print(me.getAsDict())
print()
print(me2)