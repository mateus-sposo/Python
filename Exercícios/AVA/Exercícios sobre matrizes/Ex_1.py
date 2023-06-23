l, c = map(int, input().split())
Soma = 0
VF = []
M = [list(map(int, input().split())) for _ in range(l)]
V = list(map(int, input().split()))
for i in range(l):
    for j in range(c):
        Soma += M[i][j] * V[j]
    VF.append(Soma)
    Soma = 0
print(VF)