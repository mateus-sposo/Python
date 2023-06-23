c = 1
while c != 2:     
    S = 0
    for _ in range(2):
        X = float(input())
        if X<0 or X>10:
            while X<0 or X>10:
                print("nota invalida")
                X = float(input())
                if 0<=X<=10:
                    S += X
        else:
            S += X
    M = S/2
    print(f"media = {M:.2f}")
    while c != 2:
        print("novo calculo (1-sim 2-nao)")
        c = int(input())
        if c == 1:
            S = 0
            for _ in range(2):    
                X = float(input())
                if X<0 or X>10:
                    while X<0 or X>10:
                        print("nota invalida")
                        X = float(input())
                        if 0<=X<=10:
                            S += X
                else:
                    S += X
            M = S/2
            print(f"media = {M:.2f}")
        elif c == 2:
            break