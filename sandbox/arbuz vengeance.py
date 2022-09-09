from os import system;
from random import randint;

color_set = {"R", "G", "B"};
arbuzoids = ["R"]*13 + ["G"]*17 + ["B"]*15;

found = False;
while not found:
    
    system("clear");
    #print(arbuzoids);
    r = list();
    for a in range(45):
        r.append(format(arbuzoids[a]) + ":" + format(a));
    print(r);
    print("indexes");
    ina, inb = input().split();
    a, b = int(ina), int(inb);
    
    if (arbuzoids[a] != arbuzoids[b]):
        missing = color_set.difference({arbuzoids[a], arbuzoids[b]});
        arbuzoids[a] = arbuzoids[b] = missing.pop();
    
    







