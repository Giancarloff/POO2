import requests

def stripPontos(array):
    
    for i, w in enumerate(array):
        if "," in w or "." in w:
            array[i] = w[:len(w)-1]

def contarPalavra(file):
    
    r = file.read()
    ra = r.split()
    stripPontos(ra)
    dic = dict()
    
    # gera chaves do dic
    for w in ra:
        dic[w] = 0
    
    for i, w in enumerate(ra):
        dic[w] += 1
    
    
    return dic
  
def apagarStopwords(stopwords: list[str], dic: dict()):
    
    copyDic = dict(dic)
    for k in copyDic.keys():
        #print(f"{k} in stopwords")
        #print(k in stopwords)
        if k in stopwords:
            del dic[k]
    
      

dir = "/home/giancff/Documents/POO2/POO2/exercicios/lista_3/words.txt"
file = open(dir)
dbDic = dict()

dbDic = contarPalavra(file)
print(dbDic)

url = "https://gist.githubusercontent.com/alopes/5358189/raw/2107d809cca6b83ce3d8e04dbd9463283025284f/stopwords.txt"
sw = requests.get(url).text.splitlines()

# espaços malditos
for i, w in enumerate(sw):
    sw[i] = w.strip()

#print(sw)
apagarStopwords(sw, dbDic)
print(dbDic)
