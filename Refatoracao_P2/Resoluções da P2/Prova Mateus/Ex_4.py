#Exercício 4

numero = int(input())
Dia = 1
Mosquitos_Coletados = int(input())
Menos_Mosquitos = Mosquitos_Coletados

for n in range(2,numero+1):
    Mosquitos_Coletados = int(input())
    if Mosquitos_Coletados < Menos_Mosquitos:
        Menos_Mosquitos = Mosquitos_Coletados
        Dia = n

print(f"Foram coletados {Menos_Mosquitos} mosquitos no dia {Dia}")