
def processar_venda():
    print("=== REALIZAR VENDA ===")

    produto = input("Produto: ")

    estoque = int(input("Quantidade em estoque: "))
    venda = int(input("Quantidade da venda: "))

    if venda <= estoque:
        estoque -= venda

        print("\nVenda realizada com sucesso!")
        print(f"Estoque restante: {estoque}")

    else:
        print("\nEstoque insuficiente!")

        