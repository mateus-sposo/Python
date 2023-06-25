V = int(input())
P = int(input())

def escreve(vetor):
    for i in vetor:
        print(i)

valores = [V // P] * P

if V % P != 0:
    c = 0
    while sum(valores) != V:
        valores[c] += 1
        if c == P:
            c = 0
        else:
            c += 1

escreve(valores)