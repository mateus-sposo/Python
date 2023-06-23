carros, voltas = map(int, input().split())
l1 = [0, 100000000000000000]
l2 = [0, 10000000000000000]
l3 = [0, 1000000000000000]

for i in range(carros):
    v = [int(x) for x in input().split()]
    soma = 0
    for j in range(voltas):
        soma += v[j]
    if l1[1] > soma:
        l1, l2, l3 = [i, soma], l1, l2
    elif l2[1] > soma:
        l2, l3 = [i, soma], l2
    elif l3[1] > soma:
        l3 = [i, soma]
    
print(f"{l1[0]+1}\n{l2[0]+1}\n{l3[0]+1}")