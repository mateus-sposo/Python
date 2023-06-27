N = int(input())
v = sorted([int(a) for a in input().split()])
M = [[v[0], 1]]

for i in range(1, N):
    for i in M:
        if v[i] == i[0]:
            i[1] += 1
            flag = True
            break
        else:
            flag = False
    if not flag:
        M.append([v[i], 1])

maior = [M[0][0], M[0][1]]

for i in range(1, len(M)):
    if M[i][1] > maior[1]:
        maior = [M[i][0], M[i][1]]
    elif M[i][1] == maior[1] and M[i][0] > maior[0]:
        maior = [M[i][0], M[i][1]]

print(maior[0])