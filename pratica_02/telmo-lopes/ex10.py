opcao = -1

while opcao != 0:
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", a + b)

    elif opcao == 2:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", a - b)