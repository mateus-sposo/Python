v = [int(a) for a in input().split()]

prim = v.index(1)
nono = v.index(9)

if prim > nono:
    nono, prim = prim, nono
dif = abs(prim - nono)

if prim <= 7 and nono >= 8:
    print("final")

elif dif >= 4 or (prim <= 3 and nono >= 4) or (prim <= 11 and nono >= 12):
    print("semifinal")

elif  dif >= 2 or (prim <= 1 and nono >= 2) or (prim <= 5 and nono >= 6) or (prim <= 9 and nono >= 10) or (prim <= 13 and nono >= 14):
    print("quartas")

else:
    print("oitavas")
