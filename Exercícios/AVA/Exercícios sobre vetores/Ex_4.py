from random import randint as girar
Q = 0
for _ in range(50):
    N = girar(1, 6)
    if N == 6:
        Q += 1
print(f"O número 6 foi sorteado {Q*2}% das vezes.")