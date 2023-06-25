Matriz = []
M, N = map(int, input().split())

n1, _, n2 = input().split()
Fam = [[n1, n2]]

for i in range(N-1):
    n1, _, n2 = input().split()
    Matriz.append([n1, n2])


Total = 2
c = 0

while True:
    for i in range(len(Fam[c])):
        j = 0
        while True:
            if j >= len(Matriz):
                break
            delete = False
            if Matriz[j][0] not in Fam[c] and Matriz[j][1] in Fam[c]:
                Fam[c].append(Matriz[j][0])
                Total += 1
                del(Matriz[j])
                delete = True
            elif Matriz[j][1] not in Fam[c] and Matriz[j][0] in Fam[c]:
                Fam[c].append(Matriz[j][1])
                Total += 1
                del(Matriz[j])
                delete = True
            if Total >= M:
                break
            if not delete:
                j += 1

    if Total >= M:
        break

    for i in range(len(Matriz)):
        if Matriz[i][0] not in Fam[c] and Matriz[i][1] not in Fam[c]:
            flag = True
            for j in range(c):
                if Matriz[i][0] in Fam[j] or Matriz[i][1] in Fam[j]:
                    flag = False
                    break
            if flag:
                Fam.append([Matriz[i][0], Matriz[i][1]])
                del(Matriz[i])
                c += 1
                Total += 2
                break

print(Fam, c+1)

#no beecrowd não passou, deu time limit exceeded, mas funciona