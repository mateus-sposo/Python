#Exercício 5

Numero = int(input())
Base, Lado = map(int, input().split())
Area = Base * Lado
Menor_Area = Area

for n in range(2, Numero+1):
    Base, Lado = map(int, input().split())
    Area = Base * Lado
    if  Area < Menor_Area:
        Menor_Area = Area

print(f"A menor área encontrada tem {Menor_Area} metros quadrados.")