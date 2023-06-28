N = int(input())
v = [int(a) for a in input().split()]
vf = []
vinter = []

i = 0
j = 0
p = 0

if N > 1:
    vf.append([v[0], v[1]])
    while True:
        if i < N - 1:
            dif = v[i+1] - v[i]
            j = i+1
        else:
            break
        
        while True:
            try:
                if v[j+1] - v[j] != dif:
                    vf.append([v[j], v[j+1]])
                    break
                vinter.append(v[j])
                j += 1
            except:
                break
        vf[p].append(vinter)
        i = j
        p += 1
        vinter = []
        
        if i >= N:
            break

else:
    vf.append(v[0])

print(vf)