M, N = map(int, input().split())

for i in range(M):
    vetor = [0] * M

for i in range(N):
    P, D = map(int, input().split())
    vetor[P - 1] = 1
    while True:
        if P - 1 + D < M:
            vetor[P - 1 + D] = 1
            P += D
        else:
            break
    while True:
        if P - 1 - D >= 0:
            vetor[P - 1 - D] = 1
            P -= D
        else:
            break

for i in vetor:
    print(i)