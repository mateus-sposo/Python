for _ in range(2):
    r1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    r2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    x = 1
    c = 0
    a = [1]
    V1, V2 = map(int, input().split())
    V = V1
    while V1 > 0:
        while a[c] < V1:
            a.append(2**x)
            x += 1
            c += 1
        C = len(a)
        for i in range(len(a)):
            r1[len(a)-i-1] = 1 if a[len(a)-i-1] <= V and a[len(a)-i-1] >= a[C - 2] else 0
            C -= 1
            V -= a[len(a)-i-1]
        V1 -= a[c]
    x = 1
    c = 0
    a = [1]
    V = V2
    while V2 > 0:
        while a[c] < V2:
            a.append(2**x)
            x += 1
            c += 1
        C = len(a)
        for i in range(len(a)):
            r2[len(a)-i-1] = 1 if a[len(a)-i-1] <= V and a[len(a)-i-1] >= a[C - 2] else 0
            C -= 1
            V -= a[i]
        V2 -= a[c]
    print(r1, r2)