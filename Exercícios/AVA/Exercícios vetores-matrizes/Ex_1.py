#impressão inversa de um vetor

vetor = [int(a) for a in input().split()]

vetorf = [vetor[i] for i in range(len(vetor) -1, -1, -1)]

print(vetorf)