substring = input()
string = input()

c = 0

for i in range(len(string)):
    Flag = True
    p = i
    for j in range(len(substring)):
        if Flag:
            if p + 1 <= len(string) and string[p] == substring[j]:
                p += 1
            else:
                Flag = False
        else:
            break
    if Flag:
        c += 1

print(c)