#função da distância:
def distancia (x1, y1, x2, y2):

    dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

    return dist

#função que teste se está dentro do círculo:
def estah_dentro (x1, y1, x2, y2, R):

    if distancia(x1, y1, x2, y2) > R:
        return False
    else:
        return True


#from bib_projeto import estah_dentro as dentro
def main():
    
    while True:
        valores = input().split()
        R, x1, y1 = [float(a) for a in valores[0:3]]
        N = int(valores[3])
        c = 0
        
        if R != 0:
            for _ in range(N):
                x2, y2 = map(int, input().split())
                if dentro(x1,y1,x2,y2,R) == True:
                    c += 1
                    
            print(f"Existem {c:.0f} focos nesta região.")
        
        else:
            break   

main()