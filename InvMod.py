#odwracanie modulo a*s mod b = 1
def InvMod(a,b):
    q = 0
    
    r2 = 0
    r1 = 0
    r = 0
    
    s2 = 0
    s1 = 0
    s = 0
    
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
    while r1 != 0:
        q = r2 / r1
        r = r2 - q * r1
        s = s2 - q * s1
        
        r2 = r1
        r1 = r
        s2 = s1
        s1 = s
    
    s = s1
    
    # nie istnieje
    if r1!=1:
        s = 0
        
    # ujemne s
    if s<0:
        while s<0:
            s = s + b
    
    return s


#main
invmod(5,11)