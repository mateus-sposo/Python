string = input()
Sentinela = True
i = 0

while i < len(string) and Sentinela:
    if not (ord(string[i]) >= ord("0") and ord(string[i]) <= ord("9")):
        Sentinela = False
    i += 1

if Sentinela:
    print("VERDADEIRO")
else:
    print("FALSO")