class Televisao():
    
    # 1, 2, 3, 4, 6 
    def __init__(self, ligada = False, canal = 2, tamanho = 0, marca = "", canal_minimo = 2, canal_maximo = 14) -> None:
        self.ligada = ligada;
        self.canal = canal;
        # 2
        self.tamanho = tamanho;
        self.marca = marca;
        # 4
        self.canal_minimo = canal_minimo;
        self.canal_maximo = canal_maximo;
        
    # 3
    def muda_canal_para_cima(self):
        self.canal += 1;
        # 4
        if (self.canal_maximo < self.canal):
            self.canal = self.canal_minimo;
        
    def muda_canal_para_baixo(self):
        self.canal -= 1;
        # 4
        if (self.canal < self.canal_minimo):
            self.canal = self.canal_maximo;
    
        
# 2
t1 = Televisao(False, 2, 10, "Somsung");
t2 = Televisao(False, 2, 15, "Passionfruit");

# 6
t3 = Televisao();
t3.canal_minimo = 3;
t3.canal_maximo = 23;

t4 = Televisao();
t4.canal_minimo = 1;
t4.canal_maximo = 16;

print(t1.tamanho);
print(t2.tamanho);

print(t1.marca);
print(t2.marca);


# 7

class Estado():
    
    def __init__(self, nome = "", sigla = "", cidades = list()) -> None:
        self.nome = nome;
        self.sigla = sigla;
        self.cidades = cidades;

class Cidade():
    
    def __init__(self, nome = "", populacao = 0) -> None:
        self.nome = nome;
        self.populacao = populacao;
        
cs1 = [Cidade("Abacaxilandia", 111111111), Cidade("Berchtesgaden", 111111111), Cidade("Carlostown", 111111111)];
cs2 = [Cidade("Xinpiang", 222222222), Cidade("York Nova", 222222222), Cidade("Zabuzistão", 222222222)];

e1 = Estado("Treprimoria", "TM", cs1);
e2 = Estado("Trumilandia", "TL", cs2);

pop = 0;
for c in e1.cidades:
    pop += c.populacao;

print("Populacao de " + e1.nome + " = " + format(pop));

pop = 0;
for c in e2.cidades:
    pop += c.populacao;

print("Populacao de " + e2.nome + " = " + format(pop));


# 8

class Coordenada():
    
    def __init__(self, x, y) -> None:
        self.x = x;
        self.y = y;
        
    def print_x(self) -> int:
        print(self.x);
    
    def print_y(self) -> int:
        print(self.y)
        
    def distancia(self, ponto) -> float:
        d = ((self.x - ponto.x)^2 + (self.y - ponto.y)^2)^(1/2);
        return d;
    

c0 = Coordenada(1, 1);
c1 = Coordenada(1, 0);
print(c0.distancia(c1));
        

