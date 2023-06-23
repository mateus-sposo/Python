string = input()
sentinela = True
for i in range(len(string) - 1):
    if ord(string[i]) > ord(string[i+1]):
        sentinela = False
if sentinela:
    print("CERTO")
else:
    print("ERRADO")