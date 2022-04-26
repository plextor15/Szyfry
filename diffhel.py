from abc import ABC
import math
import random
from typing import Callable

# a^b mod c
def PowerMod(a, b, c):
    if c==1: return 0
    bin_b = bin(b)
    bin_b = bin_b[2:]

    poprzedni = 1
    wielkosc = len(bin_b)
    for i in range(0, wielkosc, 1):
        if bin_b[i]=="1":
            poprzedni = (poprzedni**2) * (a**1)
        else:
            poprzedni = (poprzedni**2) * (a**0)
        poprzedni = poprzedni % c

    return poprzedni

#dzielenie metoda brute force: False - nie liczba piwerwsza / True - jest liczba piwerwsza
def BruteDzielenie(n):
    i = 2
    while i*i <= n:
        if n % i == 0 and i != n:
            return False
        i += 1

    return True

def DiffieHelman():
    g = int(input("Podaj g = "))
    
    p = int(input("Podaj p = "))
    while BruteDzielenie(p) == False:
        p = int(input("Nie podano liczby pierwszej!\n Podaj p = "))
    
    a = int(input("Podaj a (twoj secret) = "))
    A = PowerMod(g,a,p)
    print("A = ", A)
    
    B = int(input("Podaj B = "))
    k = PowerMod(B,a,p)
    print("k = ",k)
    
#main()
DiffieHelman()