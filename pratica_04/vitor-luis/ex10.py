notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]

aprovados = []
qtd_aprovados = 0

for i in notas:
    if i >= 7:
        aprovados.append(i)
        qtd_aprovados += 1

print(f"Aprovados: {aprovados}")
print(f"Quantidade de aprovados: {qtd_aprovados}")