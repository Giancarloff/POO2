from random import randint

corredores = dict()
medias = dict()
for n in range(6):
    print(f"corredor-{n+1}")
    secs = list()
    for s in range(10):
        #secs.append(int(input()))
        secs.append(randint(30, 240))
    
    sum = 0
    for s in secs:
        sum += s
    
    key = f"corredor-{n+1}"
    medias[key] = sum/len(secs)
    corredores[key] = tuple(secs)
    
min = 0
for c in corredores.values(): #fazendo o min ser o maior valor
    for n in c:
        if min < n:
            min = n

quem = None
volta = 0
for c in corredores.keys():
    for i, t in enumerate(corredores[c]):
        if t < min:
            min = t
            quem = c
            volta = i

print(f"Melhor volta: {min} secs, {quem} na volta {volta+1}")

podium = list(medias.values())
podium.sort()

for i, n in enumerate(podium): # funciona com empates mas o texto não fica correto
    print(f"{i+1} lugar ", end = "")
    for c in medias.keys():
        if (medias[c] == n):
            print(f"{c} media {n} ", end = "")
    print()
        



