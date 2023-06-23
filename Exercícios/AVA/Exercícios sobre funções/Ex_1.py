def calcula_mdc (x, y):
    
    resto = 1
    
    while resto > 0:
        resto = x%y
        x, y = y, resto
    
    return x


#from bib_projeto import calcula_mdc as mdc
def main():
    n = int(input())
    for _ in range(n):
        valores = list(map(int, input().split()))
        if mdc(valores[0], valores[1]) == 1:
            print(f"{valores[0]:.0f} {valores[1]:.0f}: primos entre si")
        else:
            print(f"{valores[0]:.0f} {valores[1]:.0f}: não primos entre si")
main()