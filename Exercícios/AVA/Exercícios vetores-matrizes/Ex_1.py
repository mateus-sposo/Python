#impressão inversa de um vetor

vetor = [int(a) for a in input().split()]
# 1 2 3 4 5 6

vetorf = [vetor[i] for i in range(len(vetor) -1, -1, -1)]
#[5, -1, -1]

print(vetorf)