from abc import ABC
import math
import random
from typing import Callable

# a^b mod c
def PowerMod(a, b, c):
    if c==1: return 0

    #zamiana z BIN na DEC
    bin_b = bin(b)
    bin_b = bin_b[2:]

    #### DEBUG ONLY ####
    #print("DEC: ", b, "    BIN: ", bin_b, "\n\n")

    poprzedni = 1
    wielkosc = len(bin_b)
    for i in range(0, wielkosc, 1):
        #postacbin[i]
        if bin_b[i]=="1":
            #print( "     ", poprzedni, "^2 * ", a, "^1 = ", poprzedni**2, " * ", a**1, " = ", (poprzedni**2) * (a**1))
            poprzedni = (poprzedni**2) * (a**1)
        else:
            #print( "     ", poprzedni, "^2 * ", a, "^0 = ", poprzedni**2, " * ", a**0, " = ", (poprzedni**2) * (a**0))
            poprzedni = (poprzedni**2) * (a**0)
        poprzedni = poprzedni % c
        #print( " ", i, "  ", bin_b[i], "  ", poprzedni )

    return poprzedni



#main()
A = 0
B = 0
C = 0
x = 0
y = 0
z = True

for i in range(0,100,1):
    A = random.randint(100, 1000)
    B = random.randint(100, 1000)
    C = random.randint(100, 1000)
    
    x = PowerMod(A,B,C)
    y = A**B%C

    if x==y: z = True
    else: z = False

    print( i, "  -  ", x, "    ", y, "    ", z )