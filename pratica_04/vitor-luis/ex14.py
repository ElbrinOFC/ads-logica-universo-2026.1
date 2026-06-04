nomes_brutos = ["  ana ", "BRUNO", "carlos", "  Maria Clara", "joão"]
notas = [7.5, 5.0, 8.0, 6.5, 9.0]
consulta = "bruno"


# ETAPA 1 - Padronizar os nomes
nomes_padronizados = []

for nome in nomes_brutos:
    nome_limpo = nome.strip().title()
    nomes_padronizados.append(nome_limpo)


# ETAPA 2 - Filtrar notas aprovadas
aprovadas = []

for nota in notas:
    if nota >= 7:
        aprovadas.append(nota)


# ETAPA 3 - Verificar presença do nome
consulta = consulta.strip().title()

encontrado = False

for nome in nomes_padronizados:
    if nome == consulta:
        encontrado = True
        break


# ETAPA 4 - Relatório final
print("===== RELATÓRIO FINAL =====")
print(f"Nomes padronizados: {nomes_padronizados}")
print(f"Notas aprovadas: {aprovadas}")

if encontrado:
    print(f"O estudante {consulta} está presente na lista")
else:
    print(f"O estudante {consulta} NÃO está presente na lista")

print(f"Quantidade de estudantes: {len(nomes_padronizados)}")
print(f"Quantidade de aprovados: {len(aprovadas)}")