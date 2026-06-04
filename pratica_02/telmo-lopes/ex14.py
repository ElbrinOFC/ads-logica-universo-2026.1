# Reescrevendo o exercício 4 com for

for _ in range(1000):  # limite alto para simular repetição
    senha = input("Digite a senha: ")
    if senha == "acesso":
        print("Acesso liberado!")
        break