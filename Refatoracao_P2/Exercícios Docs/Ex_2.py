N = int(input())
Total_Cobaias = 0
Total_Coelhos = 0
Total_Ratos = 0
Total_Sapos = 0

for n in range(N):
    Quantia, Tipo = input().split()
    Quantia = int(Quantia)
    if Tipo == "C":
        Total_Coelhos += Quantia
    elif Tipo == "R":
        Total_Ratos += Quantia
    elif Tipo == "S":
        Total_Sapos += Quantia
    Total_Cobaias += Quantia

Percentual_Coelhos = (Total_Coelhos/Total_Cobaias)*100
Percentual_Ratos = (Total_Ratos/Total_Cobaias)*100
Percentual_Sapos = (Total_Sapos/Total_Cobaias)*100

print(f"Total: {Total_Cobaias} cobaias")
print(f"Total de coelhos: {Total_Coelhos}")
print(f"Total de ratos: {Total_Ratos}")
print(f"Total de sapos: {Total_Sapos}")
print(f"Percentual de coelhos: {Percentual_Coelhos:.2f} %")
print(f"Percentual de ratos: {Percentual_Ratos:.2f} %")
print(f"Percentual de sapos: {Percentual_Sapos:.2f} %")