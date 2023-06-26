N = int(input())
vetor = input().split()
dist_max = 0

for i in range(N):
    for j in range(i+1, N):
        dist = int(vetor[i]) + int(vetor[j]) + (j-i)
        if dist > dist_max:
            dist_max = dist
print(dist_max)