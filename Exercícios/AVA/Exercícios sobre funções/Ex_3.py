def pontua_etapa(v1, v2):
    dif = v2 - v1 if v1 < v2 else v1 - v2
    if dif < 3:
        return 100
    elif dif <= 5:
        return 80
    else:
        return 80 - (dif - 5)/5


#from bib_projeto import pontua_etapa
def main():
    t1, t2, t3, e = map(int, input().split())
    maior = 0
    for _ in range(e):
        n, te1, te2, te3 = map(int, input().split())
        pontos = pontua_etapa(t1, te1) + pontua_etapa(t2, te2) + pontua_etapa(t3, te3)
        print(f"{n} {pontos:.1f}")
        if pontos > maior:
            maior = pontos
            vencedor = n
    print(f"Equipe Vencedora: {vencedor} - Pontuação: {maior:.1f}")

main()