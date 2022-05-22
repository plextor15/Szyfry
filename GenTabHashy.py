# TYLKO DO GENEROWANIA TABLICY
# uzywany jest DJB

import random
import string
#from typing import List

def bity(val, ilebit):
    return val & (2**ilebit - 1)


def DJB(stringX, ilebit=32):  #32-bit
    listaX = []
    for i in stringX:
        listaX.append(ord(i))

    hash = 5381
    for x in listaX:
        hash = hash * ilebit + hash + x
        hash = bity(hash, ilebit)
    return hash


def HashToStr(H, ileznak):
    #strX = ""
    wyjStr = ""
    wyjStr += chr(97 + (H % 26))
    for i in range(1,ileznak,1):
        wyjStr += chr(97 + int(H / 26**i)%26 )
    return wyjStr    


def HashTabGen(N,M):
    file = open("HashTab.txt", "w")
    file.write("lolxd")

    file.close()


#main
#HashTabGen(10,10)

print(HashToStr(30, 8))

#for i in range(97,123,1): print(i, " - ", chr(i))