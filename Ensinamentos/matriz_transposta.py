L, C = map(int, input().split())

M = []

def preenche_matriz(L, M):
    for i in range(L):
        valores = [int(a) for a in input().split()]
        M.append(valores)
    return M

M = preenche_matriz(L, M)
MT = []

for i in range(C):
    Linha = []
    for j in range(L):
        Linha.append(M[j][i])
    MT.append(Linha)

for i in MT:
    print(i)