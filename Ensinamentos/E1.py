L, C = map(int, input().split())
v1 = [int(a) for a in input().split()]

#1 2 3 4 5 6
#1 2
#3 4
#5 6

M1 = []
M2 = []

def preenche_matriz1 (L, C, M):
    for i in range(L):
        M.append([])
        for j in range(C):
            M[i].append(v1[i + i + j])
    return M

def preenche_matriz2(L, M):
    for i in range(L):
        valores = [int(a) for a in input().split()]
        M.append(valores)
    return M

M1 = preenche_matriz1(L, C, M1)
M2 = preenche_matriz2(L, M2)

for i in range(L):
    for j in range(C):
        M1[i][j] = M1[i][j] + M2[i][j]

print(M1)