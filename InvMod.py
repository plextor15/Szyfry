#dzielenie metoda brute force: False - nie liczba piwerwsza / True - jest liczba piwerwsza
def BruteDzielenie( n ):
    i = 2
    while i*i <= n:
        if n % i == 0 and i != n:
            return False
        i += 1

    return True

#odwracanie modulo a*s mod b = 1
def InvMod(a,b):
    if BruteDzielenie(a) == False:
        print("\n ", a, " nie jest liczba pierwsza! \n")
        return 0

    q = 0
    
    r2 = 0  # jescze bardziej poprzednia
    r1 = 0  # poprzednia
    r = 0   # akyualna
    
    s2 = 0  # jescze bardziej poprzednia
    s1 = 0  # poprzednia
    s = 0   # akyualna
    
    if a < b:
        r2 = b
        r1 = a
        s2 = 0
        s1 = 1
    else:
        r2 = a
        r1 = b
        s2 = 1
        s1 = 0
        
    #petla
    #while r1 != 0:
    while True:
        q = (int)(r2 / r1)
        r = r2 - q * r1
        s = s2 - q * s1

        if r == 0: break
        
        r2 = r1
        r1 = r
        s2 = s1
        s1 = s
    
    s = s1
    
    # nie istnieje
    if r1!=1:
        # s = 0
        print("\nNie istnieje\n")
        return 0
        
    # ujemne s
    if s<0:
        while s<0:
            s = s + b
    
    return s


#main
A = 5
B = 11
print("\n", InvMod(A, B), "\n")