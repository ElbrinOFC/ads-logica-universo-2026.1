qtd = int(input("Quantidade de alunos: "))
aprov, rec, repr = 0, 0, 0

for i in range(qtd):
    m = float(input(f"Média do aluno {i+1}: "))
    if m >= 7: aprov += 1
    elif m >= 4: rec += 1
    else: repr += 1

print(f"\nAprovados: {aprov} | Recuperação: {rec} | Reprovados: {repr}")