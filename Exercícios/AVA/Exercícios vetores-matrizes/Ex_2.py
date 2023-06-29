gabarito = input().split()

n_alunos = int(input())

for i in range(n_alunos):
    aluno = input().split()
    nota = 0
    for j in range(len(gabarito)):
        if gabarito[j] == aluno[j+1]:
            nota += 1
    print(f"Aluno: {aluno[0]}, Nota: {nota/len(gabarito)*100:.2f}%")