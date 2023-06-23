#precisa ser arrumado

M, N = map(int,input().split())
Matriz = [[]]
for i in range(N):
    l = input().split()
    flag = False
    for item in Matriz:
        if i == 0:
            Matriz = [[l[0], l[2]]]
            flag = True
            break
        elif l[0] in item:
            if l[2] not in item:
                item.append(l[2])
            flag = True
            break
        elif l[2] in item:
            item.append(l[0])
            flag = True
            break

    if not flag:
        Matriz.append([l[0], l[2]])

print(len(Matriz))