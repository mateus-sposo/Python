c = 1

while True:

    N = int(input())
    if N == 0:
        break
    
    C, M = map(int, input().split())
    maior = [[C, M]]

    for i in range(N-1):
        C, M = map(int, input().split())
        if M > maior[0][1]:
            maior = [[C, M]]
        elif M == maior[0][1]:
                maior.append([C, M])

    print(f"Turma {c}")
    for i in maior:
        print(f"{i[0]}", end=" ")
    print()
    print()
    c += 1
