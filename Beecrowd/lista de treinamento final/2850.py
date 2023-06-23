while True:
    try:
        string = input()
        if string == "esquerda":
            print("ingles")
        elif string == "direita":
            print("frances")
        elif string == "nenhuma":
            print("portugues")
        elif string == "as duas":
            print("caiu")
    except EOFError:
        break