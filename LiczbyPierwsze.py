#Sprawdzanie czy liczba jest pierwsza
# - i++ od 2 do 31 (C++) i spr brute force czy pierwsza
# - wsadzamy do Marsenna
# - to co wyjdzie brute force czy pierwsza
# - oraz testem Lukasa Lehmera

#dzielenie metoda brute force: False - nie liczba piwerwsza / True - jest liczba piwerwsza
def BruteDzielenie( n ):
    #pass
    #print("DEBUG ONLY Brute")

    #for i in range(2, n +1, 1):
    i = 2
    while i*i <= n:
        #print("debug only brute for")
        if n % i == 0 and i != n:
            return False
        i += 1

    return True


#Liczby Mersenne’a
def Mersenn( p ):
    #pass
    #wynik = 1
    #if BruteDzielenie( p ):
    #    for i in range( 0, p, 1 ):
    #        print("debug only Mersenn for")
    #        wynik *= 2
    #wynik = wynik - 1

    #wyjscie = [False, wynik]
    #if BruteDzielenie( wynik ):
    #    wyjscie[0] = True
    #else:
    #    wyjscie[0] = False

    wyjscie = [True, 1]

    for i in range( 1, p+1, 1 ):
        wyjscie[1] *= 2
    wyjscie[1] -= 1

    return wyjscie

#Metoda Lukasza Lehmera
def LukaszLehmer( P, M ):
    #pass
    S4 = 4
    Si = S4
    i = 1

    #for i in range(P-2, 0 -1, 1):
    #    print("debug only Lehmer for")
    #    Si = ((Si * Si) - 2) % M
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

print("\nZnajdywanie")
while GlownyIter <= 18:
    #prosty odsiew polowy
    #if GlownyIter % 2 == 0 and GlownyIter != 2:
        #print("DEBUG ONLY - parzysta > 2")
        #continue

    BruteTest = BruteDzielenie( GlownyIter )
    print( GlownyIter )
    if BruteTest:

        
        # I kolumna - p od Mersenna
        linijka[0] = GlownyIter
        #print("DEBUG ONLY  ")

        # II kolumna - brute dzielenie czy wynik z Mersenne'a jest liczba pierwsza
        wyjscie_M = Mersenn( GlownyIter )
        print("DEBUG ONLY  M")
        if wyjscie_M[0]:
            linijka[1] = "TAK"
        else:
            linijka[1] = "NIE"


        # III kolumna - Lukasze Lehmerem czy wynik z Mersenne'a jest liczba pierwsza
        IIIkolumna = LukaszLehmer( GlownyIter, wyjscie_M[1] )
        print("DEBUG ONLY  L")
        if IIIkolumna:
            linijka[2] = "TAK"
        else:
            linijka[2] = "NIE"

        
        #na koniec petli
        print("p = ", linijka[0], "   ", linijka[1],"   ", linijka[2])
        
    GlownyIter += 1

    #zeby nie przelatywalo za szybko
    input("")