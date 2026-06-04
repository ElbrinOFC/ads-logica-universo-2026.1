presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão".strip().title()

nomes_padronizados = []

for nome in presentes_bruto:
    nome_limpo = nome.strip().title()
    nomes_padronizados.append(nome_limpo)

encontrado = False

for i in nomes_padronizados:
    if i == consulta:
        encontrado = True
        break

if encontrado:
    print("Nome procurado encontrado!")
else:
    print("Nome não encontrado!")

print(f"Lista final: {nomes_padronizados}")
