for i in range(1, 26):
    nome_arquivo = f"ex{i}.py"
    
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("")
    
    print(f"{nome_arquivo} criado.")