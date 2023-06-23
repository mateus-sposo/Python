#Exercício 6

Numero = int(input())
Soma = 0
for n in range(1, (Numero // 2) + 1):
    Resultado = Numero % n
    if Resultado == 0:
        Soma += n
if Soma > Numero:
    print(f"{Numero} é abundante")
else:
    print(f"{Numero} não é abundante")