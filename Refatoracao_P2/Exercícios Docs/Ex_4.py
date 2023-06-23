N = int(input())
Valor = float(input())

for i in range(N):
    O = input()
    Y = float(input())
    if O == "+":
        Valor += Y
    elif O == "-":
        Valor -= Y
    elif O == "*":
        Valor *= Y
    elif O == "/":
        Valor /= Y

print(f"{Valor:.2f}")