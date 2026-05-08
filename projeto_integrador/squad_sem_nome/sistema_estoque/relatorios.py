def curva_abc():
    print("=== CURVA ABC ===")

    nome = input("Produto: ")

    quantidade = int(input("Quantidade em estoque: "))
    valor = float(input("Valor unitário: R$ "))

    total = quantidade * valor

    print(f"\nValor total em estoque: R$ {total:.2f}")

    if total >= 10000:
        classificacao = "A"

    elif total >= 5000:
        classificacao = "B"

    else:
        classificacao = "C"

    print(f"Classificação ABC: {classificacao}")