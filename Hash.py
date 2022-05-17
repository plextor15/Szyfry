def bity(val, ilebit):
    return val & (2**ilebit - 1)

def DJB(stringX):  #32-bit
    listaX = []
    for i in stringX:
        listaX.append(ord(i))

    hash = 5381
    for x in listaX:
        hash = hash * 32 + hash + x
        hash = bity(hash,32)
    return hash 

def Adler32(stringX):
    listaX = []
    for i in stringX:
        listaX.append(ord(i))
    
    A = 1
    B = 0
    P = 65521
    for x in listaX:
        A = (A+x) % P
        B = (B+A) % P
    A = bity(A,16)
    B = bity(B,16)
    hash = B * 65536 + A
    hash = bity(hash,32)
    return hash


#main
import random
import string
from typing import List
#lower_upper_alphabet = string.ascii_letters

def RandomString(ileznak):
    wynik = ''.join([random.choice(string.ascii_lowercase) for n in range(D)])
    return wynik

def duplic_index(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

M = 100000      #ile razy generujemy
D = 100         #ilu znakowe ciagi
kolizje = 0

# ---------------------------------------

print("DJB\n\n")

Wygen = []
Hashe = []

for i in range(0,M):

    l = RandomString(D)
    if l not in Wygen:
        Wygen.append(l)
    else:
        #print("BYLO")
        break

    h = DJB(l)
    if h not in Hashe:
        Hashe.append(h)
    else:
        kolizje += 1
        Hashe.append(h)
        lol = duplic_index(Hashe,h)
        print("\n\nKOLIZJA NR ", kolizje, "    ", Wygen[lol[0]], " ", Wygen[lol[1]], " ", h, "\n\n")

    if i % 1000 == 0: print("nr - ", i, "  ", l, "  ", h, "         ", len(Wygen), " , ", len(Hashe))
print(kolizje)

# -----------------------------------------

#print("Adler32\n\n")

#Wygen = []
#Hashe = []

#for i in range(0,M):

#    l = RandomString(D)
#    if l not in Wygen:
#        Wygen.append(l)
#    else:
#        #print("BYLO")
#        break

#    h = Adler32(l)
#    if h not in Hashe:
#        Hashe.append(h)
#    else:
#        kolizje += 1
#        Hashe.append(h)
#        lol = duplic_index(Hashe,h)
#        print("KOLIZJA NR ", kolizje, "    ", Wygen[lol[0]], " ", Wygen[lol[1]], " ", h, "")

#    if i % 5000 == 0: print("nr - ", i, "  ", l, "  ", h, "         ", len(Wygen), " , ", len(Hashe))
#print(kolizje)