quantidade = int(input("Digite a quantidade de números: "))

aprovados = 0
recuperaçao = 0
reprovados = 0

for i in range (quantidade):
    media = float(input("Digite a media do aluno: "))

    if media >= 7:
        aprovados += 1
    elif media >= 5:
        recuperaçao += 1
    else:
        reprovados += 1

print("Aprovados:", aprovados)
print("Recuperação:", recuperaçao)
print("Reprovados:", reprovados)