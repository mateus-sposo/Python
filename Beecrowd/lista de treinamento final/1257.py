#ord("A") = 65
#letra = ord("A") - 65

for _ in range(int(input())):
    n = int(input())
    soma = 0
    for i in range(n):
        linha = input()
        for x in range(len(linha)):
            soma += (ord(linha[x]) - 65) + i + x
    print(soma)