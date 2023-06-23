#Inserction Sort

# sourcery skip: for-index-underscore, use-itertools-product
V = [int(v) for v in input().split()]
NC = 0

for i in range(1, 10):
    NC += 1
    if V[i-1] > V[i]:
        c = i - 1
        while V[i] < V[c] and c != -1:
            c -= 1
            NC += 1
        NC += 1
        V.insert(c+1, V[i])
        del(V[i+1])

print(V)
print(NC)




#Selection Sort

V = [int(v) for v in input().split()]
NC = 0

for i in range(0, 10):
    menor = i
    for j in range(i+1, 10):
        NC += 1
        if V[j] < V[menor]:
            menor = j
    V[i], V[menor] = V[menor], V[i]

print(V)
print(NC)




#Bubble Sort

V = [int(v) for v in input().split()]
NC = 0
for i in range(0, 10):
    for j in range(0, 9):
        NC += 1
        if V[j] > V[j+1]:
            V[j], V[j+1] = V[j+1], V[j]

print(V)
print(NC)