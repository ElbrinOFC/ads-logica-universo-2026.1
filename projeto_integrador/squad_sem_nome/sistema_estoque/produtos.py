def cadastrar_produto():
    print("=== CADASTRO DE PRODUTO ===")

    nome = input("Nome do produto: ")

    quantidade = int(input("Quantidade: "))

    validade = input("Data de validade: ")

    print("\nProduto cadastrado com sucesso!")
    print(f"Produto: {nome}")
    print(f"Quantidade: {quantidade}")
    print(f"Validade: {validade}")