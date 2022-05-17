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


M = 100000      #ile razy generujemy
D = 8         #ilu znakowe ciagi
kolizje = 0


ListaHashy = []
ListaWygen = []

for i in range(M):
    ll = RandomString(D)
    if ll not in ListaWygen:
        ListaWygen.append(ll)

I = 0
for i in ListaWygen:
    h = DJB(ListaWygen[I])
    if h not in ListaHashy:
        ListaHashy.append(h)
    else:
        kolizje += 1
        ListaHashy.append(h)
    I += 1

#print( ListaWygen )
#print( ListaHashy )
print( kolizje )