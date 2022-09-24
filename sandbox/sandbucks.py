dir = "/home/giancff/Documents/POO2/POO2/sandbox/words.txt"
f = open(dir)
#print(f.read())

r = f.read()
ra = r.split()

for w in ra:
    print(w)

