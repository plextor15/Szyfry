# TYLKO DO GENEROWANIA TABLICY
# uzywany jest DJB

import random
import string
#from typing import List

def bity(val, ilebit):
    return val & (2**ilebit - 1)


def RandomString(ileznak):
    wynik = ''.join([random.choice(string.ascii_lowercase) for n in range(ileznak)])
    return wynik


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
    wyjStr += chr(97 + int(H % 26))
    for i in range(1,ileznak,1):
        wyjStr += chr(97 + int(H / 26**i)%26 )
    return wyjStr    


def HashTabGen(N, M, ileznak):
    file = open("HashTab.txt", "w")
    TablicaHashy = []                               #zeby nie bylo duplikatow
    TablicaSpr = []
    TablicaElem = [] #Pierwszy element w wierzu
    dlugosc = 0

    while dlugosc <= M:
        PierStrWiersz = RandomString(ileznak)
        StrWiersz = PierStrWiersz
        JegoHash = DJB( StrWiersz, 32 )

        #hc = 0
        Wiersz = []
        for n in range(N):
            StrWiersz = HashToStr( int(JegoHash), ileznak)
            Wiersz.append( StrWiersz )

            JegoHash = str(DJB(StrWiersz, ileznak))
            Wiersz.append( JegoHash )

            #hc = 1
        if Wiersz[N-1] not in TablicaSpr:   #usuwanie takich samych koncowek
            TablicaHashy.append( Wiersz )

            TablicaSpr.append( JegoHash )
            TablicaElem.append( PierStrWiersz )
            print(" - ", PierStrWiersz, "  ", JegoHash)
        dlugosc += 1
        
    
    for i in range( len(TablicaElem) ):
        dowpisania = "" + TablicaElem[i] + " " + TablicaSpr[i] + "\n"
        file.write( dowpisania )

    file.close()


#main

#print(HashToStr(30, 8))
#for i in range(97,123,1): print(i, " - ", chr(i))

HashTabGen(500, 200, 8)