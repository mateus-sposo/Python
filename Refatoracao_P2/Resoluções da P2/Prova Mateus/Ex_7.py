#Exercício 7

string = input()
Sentinela = True

for charac in string:
    if (ord(charac) < ord("a") or ord(charac) > ord("z")) and (ord(charac) < ord("A") or ord(charac) > ord("Z")):
        Sentinela = False
        break

if Sentinela:
    print("VERDADEIRO")
else:
    print("FALSO")