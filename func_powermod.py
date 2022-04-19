import math

# a^b mod c
def PowerMod(a, b, c):
    pass

    if c==1:
        return 0

    #zamiana z BIN na DEC
    bin_b = bin(b)
    bin_b = bin_b[2:]

    #### DEBUG ONLY ####
    print("DEC: ", b, "    BIN: ", bin_b, "\n\n")
    
    #liczby_do_zpot = []
    #wielkosc = len(bin_b)
    #pot = wielkosc-1
    #for i in range(0, wielkosc, 1):
    #    if bin_b[i] == '1':
    #        liczby_do_zpot.append(pow(2,pot))
    #    pot -= 1 
    #maxwykladnik = len(bin_b)

    poprzedni = 1
    wielkosc = len(bin_b)
    for i in range(0, wielkosc, 1):
        #postacbin[i]
        if bin_b[i]=="1":
            print( "     ", poprzedni, "^2 * ", a, "^1 = ", poprzedni**2, " * ", a**1, " = ", (poprzedni**2) * (a**1))
            poprzedni = (poprzedni**2) * (a**1)
        else:
            print( "     ", poprzedni, "^2 * ", a, "^0 = ", poprzedni**2, " * ", a**0, " = ", (poprzedni**2) * (a**0))
            poprzedni = (poprzedni**2) * (a**0)
        poprzedni = poprzedni % c
        print( " ", i, "  ", bin_b[i], "  ", poprzedni )

    return poprzedni






#main()
lol = PowerMod(3,17,25)
#for i in range(len(lol)): 
#    print(lol[i])

print(lol)
print(3**17%25)