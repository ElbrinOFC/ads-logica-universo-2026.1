nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o seu ano de nacsmento: "))
altura = float(input("Digite a sua altura: "))

idade = 2026 - ano_nascimento

print(f"Olá, {nome}! Você tem {idade} anos e sua altura é de {altura:.2f}m. Regitro concluido.")