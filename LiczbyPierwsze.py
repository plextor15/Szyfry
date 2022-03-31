#Sprawdzanie czy liczba jest pierwsza
# - i++ od 2 do 31 (C++) i spr brute force czy pierwsza
# - wsadzamy do Marsenna
# - to co wyjdzie brute force czy pierwsza
# - oraz testem Lukasa Lehmera

#dzielenie metoda brute force: False - nie liczba piwerwsza / True - jest liczba piwerwsza
def BruteDzielenie( n ):
    #pass
    #print("DEBUG ONLY Brute")
    for i in range(2, n +1, 1):
        print("debug only brute for")
        if n % i == 0:
            if i == n:
                return True
            else:
                return False

#Liczby Mersenne’a
def Mersenn( p ):
    #pass
    wynik = 2
    if BruteDzielenie( p ):
        for i in range( 0, p, 1 ):
            print("debug only Mersenn for")
            wynik *= 2
    wynik = wynik - 1

    wyjscie = [False, wynik]
    if BruteDzielenie( wynik ):
        wyjscie[0] = True
    else:
        wyjscie[0] = False

    return wyjscie

#Metoda Lukasza Lehmera
def LukaszLehmer( P, M ):
    #pass
    S4 = 4
    Si = S4

    for i in range(P-2, 0 -1, 1):
        print("debug only Lehmer for")
        Si = ((Si * Si) - 2) % M

    if Si == 0:
        return True
    else:
        return False


#main()
GlownyIter = 2
BruteTest = False
linijka = [0, "NIE", "NIE"]

print("\nZnajdywanie")
while GlownyIter <= 7:
    #prosty odsiew polowy
    #if GlownyIter % 2 == 0 and GlownyIter != 2:
        #print("DEBUG ONLY - parzysta > 2")
        #continue

    BruteTest = BruteDzielenie( GlownyIter )
    if BruteTest:

        print("DEBUG ONLY  ")
        # I kolumna - p od Mersenna
        linijka[0] = GlownyIter

        # II kolumna - brute dzielenie czy wynik z Mersenne'a jest liczba pierwsza
        wyjscie_M = Mersenn( GlownyIter )
        print("DEBUG ONLY  ")
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
        print("p = ", linijka[0], "   ", linijka[1],"   ", linijka[2], "\n")
        GlownyIter += 1