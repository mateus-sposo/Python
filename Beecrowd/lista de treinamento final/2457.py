letra = input()
linha = input().split()
c = 0

for i in linha:
    if letra in i:
        c += 1

porcentagem = (c/len(linha))*100

print(f"{porcentagem:.1f}")