permutacao = input()
string = input()

nova_str = ""

#ord(a) == 97

for i in string:
    for j in range(len(permutacao)):
        if i == permutacao[j]:
            p = j
            break
    nova_str += chr(p+97)

print(nova_str)
