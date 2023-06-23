#Exercício 2

Numero = int(input())
if Numero > 0: 
    print("Positivo")
    if Numero%2 == 0:
        print("Par")
    else:
        print("Ímpar")
elif Numero < 0:
    print("Negativo")
    if Numero%2 == 0:
        print("Par")
    else:
        print("Ímpar")
else:
    print("Zero")
    print("Par")