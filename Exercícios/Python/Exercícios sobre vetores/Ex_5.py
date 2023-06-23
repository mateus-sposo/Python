vet = input().split()
vet = [int(i) for i in vet]
pos = []
semdup = []
for i in range(len(vet)):
    if vet[i] > 0:
        pos.append(vet[i])
for i in range(len(pos)):
    if pos[i] not in semdup:
        semdup.append(pos[i])
print("vet =", vet)
print("pos =", pos)
print("semdup =", semdup)