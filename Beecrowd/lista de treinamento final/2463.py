N = int(input())
v = [int(a) for a in input().split()]

maior, somaf = 0, 0

for i in range(N):
    maior = max(0, maior + v[i])
    somaf = max(somaf, maior)

print(somaf)