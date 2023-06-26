#incompleto

N = int(input())
vetor = [int(a) for a in input().split()]
dist_max = 0
maior = 0

for i in range(N):
    if vetor[i] > maior:
        maior = vetor[i]
        p = i

for i in range(N):
    if maior + vetor[i] + abs(p-i) > dist_max:
        dist_max = maior + vetor[i] + abs(p-i)

print(dist_max)