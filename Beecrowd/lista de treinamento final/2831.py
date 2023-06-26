N = int(input())
v = sorted([int(a) for a in input().split()])

if N == 1:
    if v[0] <= 8:
        flag = True
    else:
        flag = False

elif v[0] > 8:
    flag = False

else:
    for i in range(1, N):
        flag = False
        if v[i] - v[i-1] <= 8:
            flag = True
        else:
            flag = False
            break

if flag:
    print("S")
else:
    print("N")