qtd = int(input("Quantidade de alunos: "))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(qtd):
    media = float(input("Digite a média: "))

    if media >= 7:
        aprovados += 1
    elif media >= 4:
        recuperacao += 1
    else:
        reprovados += 1

print("Aprovados:", aprovados)
print("Recuperação:", recuperacao)
print("Reprovados:", reprovados)