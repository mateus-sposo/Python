'''Minha biblioteca de funções'''
'''-----------------------------------------------------------------------------------------------------------------'''
#funções para calculos matematicos

#media de um vetor de numeros
def media_vetor (vetor):  # sourcery skip: simplify-generator, sum-comprehension
    soma = 0
    for i in vetor:
        soma += i
    return (soma/len(vetor))

#area de um quadrilatero
def area_quadrilatero (base, altura):
    return (base*altura)

#area de um triangulo
def area_triangulo (base, altura):
    return ((base*altura)/2)

#area de um circulo
def area_circulo (pi, raio):
    return (pi*(raio**2))

#area de um trapezio
def area_trapezio (base_maior, base_menor, altura):
    return (((base_maior + base_menor)*altura)/2)

#hipotenusa de um triangulo
def hipotenusa_triangulo (cateto1, cateto2):
    return (((cateto1**2) + (cateto2**2))**(1/2))

#cateto de um triangulo
def cateto_triangulo (hipotenusa, cateto):
    return (((hipotenusa**2) - (cateto**2))**(1/2))

#raizes de uma equacao de segundo grau
def raizes_equacao_segundo_grau(a, b, c):
    delta = (b**2 - 4 * a * c)
    if delta >= 0:
        return [((-b) + delta)/(2 * a), ((-b) - delta)/(2 * a)]
    else:
        return ("Não há raizes reais")

#soma de uma progressão aritmetica
def soma_pa (vetor):
    n = len(vetor)
    a1 = vetor[0]
    an = vetor[n-1]
    return ((a1 + an)*n/2)

#soma de uma progressão geometrica
def soma_pg (vetor):
    n = len(vetor)
    a1 = vetor[0]
    r = vetor[1]/vetor[0]
    return ((a1 * (r**n - 1))/(r - 1))

#verifica se um numero é primo
def primo (numero):
    if numero == 1:
        return False
    for i in range(2, numero//2 + 1):
        if numero % i == 0:
            return False
    return True

'''-----------------------------------------------------------------------------------------------------------------'''
#funções para manipulação de strings

#verifica se uma string é palindromo
def palindromo (string):
    invstring = string[::-1]
    return (string == invstring)

#verifica se uma string é um anagrama
def anagrama (string1, string2):
    if len(string1) != len(string2):
        return False 
    for i in string1:
        if i not in string2:
            return False
    return True

#lista todas as permutações de uma string
def permutacoes (string):
    if len(string) == 1:
        return [string]
    else:
        perm = []
        for i in range(len(string)):
            for j in permutacoes(string[:i] + string[i+1:]):
                if string[i] + j not in perm:
                    perm.append(string[i] + j)
        return perm
