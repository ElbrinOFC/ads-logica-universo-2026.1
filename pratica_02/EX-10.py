opcao = -1

while opcao != 0:
    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("0 - sair")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print("Resultado:", n1 + n2)

    elif opcao == 2:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print("Resultado:", n1 - n2)

    elif opcao == 3:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print("Resultado:", n1 * n2)

    elif opcao == 0:
        print("Programa encerrado")

    else:
        print("Opcao invalida")