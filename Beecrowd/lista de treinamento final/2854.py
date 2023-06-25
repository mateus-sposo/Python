Matriz = []
M, N = map(int, input().split())

n1, _, n2 = input().split()
Fam = [[n1, n2]]

for i in range(N-1):
    n1, _, n2 = input().split()
    Matriz.append([n1, n2])

def check(Matriz, Fam, C, c, Total):
    flag = True
    for j in range(c):
        if Matriz[i][0] in Fam[j] or Matriz[i][1] in Fam[j]:
            flag = False
            break
    if flag:
        Fam.append([Matriz[i][0], Matriz[i][1]])
        del(Matriz[i])
        C += 1
        Total += 2
    return Matriz, Fam, C, Total

Total = 2
c = 0
C = 0
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
            elif Matriz[j][0] in Fam[c]:
                del(Matriz[j])
                delete = True
            elif C == c:
                Matriz, Fam, C, Total = check(Matriz, Fam, C, c, Total)
            if Total >= M:
                break
            if not delete:
                j += 1
        if Total >= M:
            break
    c = int(C)
    
    if Total >= M:
        break

print(Fam, c+1)

#no beecrowd não passou, deu time limit exceeded, mas funciona