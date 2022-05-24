#druga czesc do GenTabHash

import random
import string
from typing import List


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


def RandomString(ileznak):
    wynik = ''.join([random.choice(string.ascii_lowercase) for n in range(D)])
    return wynik


def HashToStr(H, ileznak):
    #strX = ""
    wyjStr = ""
    wyjStr += chr(97 + int(H % 26))
    for i in range(1,ileznak,1):
        wyjStr += chr(97 + int(H / 26**i)%26 )
    return wyjStr


M = 10000      #ile razy generujemy
D = 8         #ilu znakowe ciagi
kolizje = 0

# ---------------------------------------


#print("Adler32\n\n")

WygenStr = []
WygenHa = []
#Hashe = []
#Powt = []
#wynikowystring = "DJB\n"

for i in range(0,M):
    l = RandomString(D)
    if l not in WygenStr:
        h = DJB(l)
        WygenStr.append(l)
        WygenHa.append(h)

print("Wygen\n")


file = open("HashTablicaSkrocone.txt", "r")
#Line = file.readline()
HashTabStr = []
HashTabHa = []
for Line in file:
    #Wiersz = Line
    fString = Line[0:8]
    fHash = int(Line[9:-1])
    #print( fString + "-" + str(fHash) ) #DEBUG ONLY!!
    HashTabStr.append(fString)
    HashTabHa.append(fHash)
    print(fString, str(fHash)) #DEBUG ONLY

file.close()


SkroconaTab = []
Wiersz = []
aktualHash = 0
aktualString = HashTabStr[0]

for hStr in HashTabStr:
    Wiersz = []
    #print(hStr)
    aktualString = hStr
    for l in range(10000):
        Wiersz.append(aktualString)
        aktualHash = DJB(aktualString)
        Wiersz.append(aktualHash)
        aktualString = HashToStr(aktualHash, 8)
    SkroconaTab.append(Wiersz)

    strtmp = ""
    for i in range(1,10,2):
        strtmp += str(Wiersz[i]) + " "
    print(strtmp)
print("Odbudowany")


#print(HashTab) #DEBUG ONLY!!
file2 = open("Kolizje.txt", "x")

Kolizje = []
kolizjeString = ""

for i in range( 0, len(WygenStr) ):
    print("- ",i,"/",len(WygenStr))  #DEBUG ONLY!!

    NIEznaleziony = True
    for j in range( 0, len(HashTabHa) ):
        #print("-- ",j,"/",len(HashTabHa))  #DEBUG ONLY!!
        if WygenHa[i] == HashTabHa[j]:
            NIEznaleziony = False
            kolizjeString = WygenStr[i] + "  " + str(HashTabHa[j]) + "  " + HashTabStr[j]
            Kolizje.append(kolizjeString)

            kolizjeString += "\n"
            file2.write(kolizjeString)
            print( kolizjeString )  #DEBUG ONLY!!
            break

    if NIEznaleziony:
        for x in SkroconaTab:
            for l in range(1, 10000, 2):
                if x[l] == WygenHa[i]:
                    NIEznaleziony = False

                    kolizjeString = WygenStr[i] + "  " + str(HashTabHa[i]) + "  " + x[l-1] + "z ciagu"
                    Kolizje.append(kolizjeString)

                    kolizjeString += "\n"
                    file2.write(kolizjeString)
                    break
                

            if not(NIEznaleziony):
                break

        #for x in SkroconaTab:
        #    for l in range(0, 10000, 2):
        #        if x[l] == WygenHa[i]:
        #            NIEznaleziony = False

        #            kolizjeString = WygenStr[i] + "  " + str(HashTabHa[i]) + "  " + x[l-1] + "z ciagu"
        #            Kolizje.append(kolizjeString)

        #            kolizjeString += "\n"
        #            file2.write(kolizjeString)
        #            break
                

        #    if not(NIEznaleziony):
        #        break













        ##aktualHash = WygenHa[i]
        #aktualHash = 0
        #aktualString = HashTabStr[0]

        #for j in range( 0, len(HashTabHa) ):
        #    for l in range(10000):
        #        aktualHash = DJB(aktualString)
        #        aktualString = HashToStr(aktualHash, 8)
                
        #        if aktualHash == WygenHa[i]:
        #            NIEznaleziony = False

        #            kolizjeString = WygenStr[i] + "  " + str(HashTabHa[i]) + "  " + aktualString + "z ciagu"
        #            Kolizje.append(kolizjeString)

        #            kolizjeString += "\n"
        #            file2.write(kolizjeString)
        #            break
        #        l += 1

        #    if not(NIEznaleziony):
        #        break
    
file2.close()
for i in Kolizje: print(i)