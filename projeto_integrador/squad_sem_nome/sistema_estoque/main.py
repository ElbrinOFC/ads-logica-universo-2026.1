from produtos import cadastrar_produto
from movimentacao import processar_venda
from relatorios import curva_abc
from utils import limpar_tela

while True:
    print("\n=== SISTEMA DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Realizar venda")
    print("3 - Relatório Curva ABC")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        limpar_tela()
        cadastrar_produto()

    elif opcao == "2":
        limpar_tela()
        processar_venda()

    elif opcao == "3":
        limpar_tela()
        curva_abc()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")