opcao = -1

while opcao != 0:
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        print("Resultado: ", num1 + num2)

    elif opcao == 2:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        print("Resultado: ", num1 - num2)

    elif opcao == 0:
        print("Programa encerrado.")
        
    else:
        print("Opcao invalida")