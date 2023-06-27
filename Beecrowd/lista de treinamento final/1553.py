while True:
    N, K = map(int, input().split())

    if N == K == 0:
        break

    v = [int(a) for a in input().split()]
    M = [[v[0], 1]]
    for i in range(1, N):
        flag = False
        for j in range(len(M)):
            if v[i] == M[j][0]:
                p = j
                flag = True
                break
        if flag:
            M[p][1] += 1
        else:
            M.append([v[i], 1])

    c = sum(1 for i in M if i[1] >= K)
    print(c)

    c = 0

    for i in M:
        if i[1] >= K:
            c += 1
    
    print(c)

