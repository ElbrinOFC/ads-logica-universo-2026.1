print("Exercício 10")

opcao = -1

while opcao != 0:
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))
        print("Resultado:", a + b)

    elif opcao == 2:
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))
        print("Resultado:", a - b)