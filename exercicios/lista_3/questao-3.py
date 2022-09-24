notas = list()
alunos = dict()

inc = None
print("nome nota1 nota2")
while inc != []:
    inc = input().strip().split()
    # print(inc) debug
    if inc != []:
        alunos[inc[0]] = (float(inc[1]), float(inc[2]))
    
print("digite o nome para saber a nota")
n = None
while n != '':
    n = input()
    if n in alunos.keys():
        media = float( (alunos[n][0] + alunos[n][1])/2 )
        print(media)
    else:
        print("não é aluno")
    

