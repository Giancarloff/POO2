# assumi que vogal na verdade é a palavra

def contarPalavra(file):
    
    r = file.read()
    ra = r.split()
    dic = dict()
    
    # gera chaves do dic
    for w in ra:
        dic[w] = 0
    
    for i, w in enumerate(ra):
        if "," in w or "." in w:
            ra[i] = w[:len(w)-1]
        
        dic[w] += 1
    
    
    print(dic)
    

dir = "/home/giancff/Documents/POO2/POO2/exercicios/lista_3/words.txt"
file = open(dir)

contarPalavra(file)




