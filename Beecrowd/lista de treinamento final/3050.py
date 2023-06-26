#incompleto

N = int(input())
vetor = [int(a) for a in input().split()]
dist_max = 0
maior = 0

for i in range(N):
    if vetor[0] + vetor[i] + i > maior:
        maior = vetor[i] + vetor[0] + i
        p = i

for i in range(N):
    if vetor[p] + vetor[i] + abs(p-i) > dist_max:
        dist_max = vetor[p] + vetor[i] + abs(p-i)

print(dist_max)