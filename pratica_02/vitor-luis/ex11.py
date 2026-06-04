# ex11.py
# Classificação da turma

cont_aprovados = 0
cont_recuperacao = 0
cont_reprovados = 0

qtd_alunos = int(input("Digite a quantidade de alunos: "))

for i in range(qtd_alunos):
    media = float(input(f"Digite a média do aluno {i + 1}: "))

    if media >= 7:
        cont_aprovados += 1
    elif media >= 4 and media < 7:
        cont_recuperacao += 1
    else:
        cont_reprovados += 1

print(f"Aprovados: {cont_aprovados}")
print(f"Em recuperação: {cont_recuperacao}")
print(f"Reprovados: {cont_reprovados}")
