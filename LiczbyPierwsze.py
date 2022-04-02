#Sprawdzanie czy liczba jest pierwsza
# - i++ od 2 do 31 (C++) i spr brute force czy pierwsza
# - wsadzamy do Marsenna
# - to co wyjdzie brute force czy pierwsza
# - oraz testem Lukasa Lehmera
# Dodatkowe inne bajery

#import time

#dzielenie metoda brute force: False - nie liczba piwerwsza / True - jest liczba piwerwsza
def BruteDzielenie( n ):
    i = 2
    while i*i <= n:
        if n % i == 0 and i != n:
            return False
        i += 1

    return True


#Liczby Mersenne’a
def Mersenn( p ):
    wyjscie = [True, 1]

    for i in range( 1, p+1, 1 ):
        wyjscie[1] *= 2
    wyjscie[1] -= 1

    return wyjscie

#Metoda Lukasza Lehmera
def LukaszLehmer( P, M ):
    S4 = 4
    Si = S4
    i = 1

    while i <= P-2:
        Si = ((Si * Si) - 2) % M
        i += 1

    if Si % M == 0:
        return True
    else:
        return False


#main()
GlownyIter = 2
BruteTest = False
linijka = [0, "NIE", "NIE"]

print("\nZnajdywanie Liczb")
while GlownyIter <= 31:
#while True:
    #start_time = time.time()

    BruteTest = BruteDzielenie( GlownyIter )
    #print( GlownyIter )
    if BruteTest:

        
        # I kolumna - p od Mersenna
        linijka[0] = GlownyIter

        # II kolumna - brute dzielenie czy wynik z Mersenne'a jest liczba pierwsza
        wyjscie_M = Mersenn( GlownyIter )
        if wyjscie_M[0]:
            linijka[1] = "TAK"
        else:
            linijka[1] = "NIE"


        # III kolumna - Lukasze Lehmerem czy wynik z Mersenne'a jest liczba pierwsza
        IIIkolumna = LukaszLehmer( GlownyIter, wyjscie_M[1] )
        if IIIkolumna:
            linijka[2] = "TAK"
        else:
            linijka[2] = "NIE"

        
        #na koniec petli
        #print("p = ", linijka[0], "   ", linijka[1],"   ", linijka[2], "        czas:", " %s s" % (time.time() - start_time))
        print("p = ", linijka[0], "   ", linijka[1],"   ", linijka[2])
        
    GlownyIter += 1