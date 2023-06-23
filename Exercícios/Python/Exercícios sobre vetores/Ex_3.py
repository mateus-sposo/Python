Vetor = input().split()
X = input()
Flag = False
for i in range(len(Vetor)):
    if Vetor[i] == X:
        P = i + 1
        Flag = True
        break
if Flag:
    print(P)
else:
    print(-1)