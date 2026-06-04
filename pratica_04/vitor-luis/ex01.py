nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]
nomes_padronizados = []

for nome in nomes_brutos:
    nome_limpo = nome.strip().title()
    nomes_padronizados.append(nome_limpo)

print(f"Nomes: {nomes_padronizados}")
print(f"Quantidade de nomes: {len(nomes_padronizados)}")