mosquitos = 0
total = 0

Numero = int(input())

for dia in range(Numero):
    mosquitos = int(input())
    total += mosquitos

media = total / Numero

print (f'Foram coletados {total} mosquitos em {Numero} dias')
print (f'Média diária de {media:.1f} mosquitos')