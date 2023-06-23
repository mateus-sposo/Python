for _ in range(int(input())):
    linha = input().lower()
    linha = list(linha)
    Matriz = []
    flag = True

    for item in linha:
        if item in "abcdefghijklmnopqrstuvwxyz":
            for item_ in Matriz:
                if item == item_[0]:
                    item_[1] += 1
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                Matriz.append([item, 1])

    maior = [Matriz[0]]
    for item in Matriz:
        if item[1] > maior[0][1]:
            maior = [item]
        elif item[1] == maior[0][1]:
            maior.append(item)

    vetor = sorted({i[0] for i in maior})

    for i in vetor:
        print(i, end="")
    print()



#outra tentativa:

for _ in range(int(input())):
    linha = sorted(input().lower())
    linha = [i for i in linha if i in "abcdefghijklmnopqrstuvwxyz"]
    string = linha[0]
    for i in range(len(linha)-1):
        if linha[i] != linha[i+1]:
            string += " "
        string += linha[i+1]

    linha = string.split()
    maior = [linha[0]]
    for i in range(1, len(linha)):
        if len(maior[0]) < len(linha[i]):
            maior = [linha[i]]
        elif len(maior[0]) == len(linha[i]):
            maior.append(linha[i])

    linha = [set(i) for i in maior]
    string = ""
    for i in linha:
        string += list(i)[0]
    print(string)