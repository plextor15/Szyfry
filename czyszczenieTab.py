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


file = open("HashTablicaExported_.txt","r")

HashTabStr = []
HashTabHa = []

for Line in file:
    fString = Line[0:8]
    fHash = Line[9:-1]
    HashTabStr.append(fString)
    HashTabHa.append(fHash)
file.close()

#indexy = []
#for y in HashTabHa:
#    print(" - ") #DEBUG ONLY
#    indexy = duplic_index( fHash, y )
#    if len(indexy) > 1:
#        del indexy[0]
#        for x in range(len(indexy)):
#            HashTabHa.pop(x)
#            HashTabStr.pop(x)
#    #for i in range(len(HashTabHa)):
#    #    pass

HashTabStr2 = list(dict.fromkeys(HashTabStr))
HashTabHa2 = list(dict.fromkeys(HashTabHa))

file2 = open("HashTablicaSkrocone.txt","x")
for i in range(len(HashTabHa2)):
    dowpisania = "" + HashTabStr2[i] + " " + HashTabHa2[i] + "\n"
    file2.write( dowpisania )
file2.close()