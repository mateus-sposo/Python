Gravidade = 9.8
Pesado = 500.0
Leve = 100.0

peso = 0.0
massa = 0.0

massa = float(input())

peso = massa * Gravidade

print ('Peso do objeto: ', format(peso, '.2f'))
if peso > Pesado:
    print ('Objeto muito pesado.')
elif  peso < Leve:
    print ('Objeto muito leve.')