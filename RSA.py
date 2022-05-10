def NWD(a, b):
    if b > 0:
        return NWD(b, a%b)
    else:
        return a

def BruteDzielenie( n ):
    i = 2
    while i*i <= n:
        if n % i == 0 and i != n:
            return False
        i += 1

    return True

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
        if bin_b[i]=="1":
            poprzedni = (poprzedni**2) * (a**1)
        else:
            poprzedni = (poprzedni**2) * (a**0)
        poprzedni = poprzedni % c

    return poprzedni

def InvMod(a,b):
    #if BruteDzielenie(a) == False:
        #print("\n ", a, " nie jest liczba pierwsza! \n") #DEBUG ONLY!!
        #return 0

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
        #print("\nNie istnieje\n") #DEBUG ONLY!!
        return 0
        
    # ujemne s
    if s<0:
        while s<0:
            s = s + b
    
    return s

#import random
def RSA(p,q,e,m, tryb):     # tryb - True szyfrowanie / False odszyfrowanie (wtedy m to c)
    if BruteDzielenie(p) == False:
        return -1
    if BruteDzielenie(q) == False:
        return -1    
    
    n = p*q    
    fi = (p-1)*(q-1)
    
                        #print("p: ", p, "q: ", q, "e: ", e)
                        #e = random.randint(1,fi)
                        #while(NWD(e,fi) != 1):
                        #    e = random.randint(1,fi)

    if e <= 1 or e >= fi:
        print("Zla wartosc e!")
        return 0

    if NWD(e,fi) != 1:
        print("-- NWD(e,fi) != 1 --")
        return 0

    d = InvMod(e,fi)
    
    c = PowerMod(m,e,n)
    #print("d: ", d, "m: ", m, "c: ", c)
    
    m2 = PowerMod(c,d,n)
    #print(m2)

    if tryb: return c
    else: return m2




#main
Tekst = "Ala ma kota"
TekstSzyf = []
TekstInt1 = []
TekstRSA = []
TekstInt2 = []
TekstOdsz = []

#RSA
p_ = 17
q_ = 29
print("p = ",p_,", q = ", q_)

n_ = p_*q_
print("n = ", n_)

fi_  = (p_-1)*(q_-1)
print("fi(n) = ", fi_)

e_ = 419  #pub
print("e = ", e_)

d_ = InvMod(e_,fi_) #priv
print("d = ", d_)

print("\n")
for i in Tekst:
    #print(i)
    TekstSzyf.append(i)
    i = ord(i)
    #print(i)  #DEBUG ONLY!!
    TekstInt1.append(i)

    #i = RSA(p_,q_,e_,i,True)
    i = PowerMod(i,e_,n_)
    TekstRSA.append(i)

    #i = RSA(p_,q_,e_,i,False)
    i = PowerMod(i,d_,n_)
    TekstInt2.append(i)

    i = chr(i)
    TekstOdsz.append(i)

    
print( TekstSzyf )
print( TekstInt1 )
print( TekstRSA )
print( TekstInt2 )
print( TekstOdsz )