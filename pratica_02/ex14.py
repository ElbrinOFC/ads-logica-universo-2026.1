print("Exercício 14")

# Usando for no lugar de while

for _ in range(1000):  # limite alto só pra garantir repetição
    senha = input("Digite a senha: ")
    if senha == "acesso":
        print("Acesso liberado!")
        break