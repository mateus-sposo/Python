Vetor = input().split()
VetorF = []
for i in range(len(Vetor)):
    for c in range(i+1, len(Vetor)):
        if float(Vetor[i]) > float(Vetor[c]):
            Vetor[i], Vetor[c] = Vetor[c], Vetor[i]
for i in range(len(Vetor) - 1):
    if Vetor[i] != Vetor[i + 1]:
        VetorF.append(Vetor[i])
if len(Vetor) > 0:
    print(len(VetorF) + 1)
else:
    print(len(VetorF))