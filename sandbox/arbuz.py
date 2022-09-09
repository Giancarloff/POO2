import os
from random import randint

color_set = {"R", "G", "B"};
arbuzoids = ["R"]*13 + ["G"]*17 + ["B"]*15;

# não tem como todos os arbuzoids serem iguais
# pois deveria haver um caso onde duas cores tem o mesmo número de zoides
# e com esse estado inicial, isso é impossível

all_R = ["R"]*45;
all_G = ["G"]*45;
all_B = ["B"]*45;

#print(arbuzoids);

found = False;
loop = 0;
last_a = last_b = -1;
while not found:
    
    os.system("clear");
    loop += 1;
    print(loop);
    a, b = randint(0, 44), randint(0, 44);
    
    if arbuzoids[a] != arbuzoids[b]:
        missing = color_set.difference({arbuzoids[a], arbuzoids[b]});
        #print(missing);
        arbuzoids[a] = arbuzoids[b] = missing.pop();
        #print(arbuzoids);
        #input()
        
    if (arbuzoids == all_R or arbuzoids == all_G or arbuzoids == all_B):
        found = True;
        print("Found at loop " + format(loop));