# ex10.py
# Menu simples

opcao = -1
operacao = 0

while opcao != 0:
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Encerrar")
    opcao = int(input())

    if opcao == 1:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        operacao = num1 + num2

    elif opcao == 2:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        operacao = num1 - num2

    elif opcao == 0:
        print("Encerrando...")
        break

    else:
        print("Opção inválida")

    print(f"{operacao}")
