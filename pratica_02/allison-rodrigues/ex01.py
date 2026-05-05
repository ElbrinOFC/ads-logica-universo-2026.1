# pede o nome (texto)
nome = input("Digite seu nome: ")

# pede o ano e converte para inteiro
ano_nascimento = int(input("Digite seu ano de nascimento: "))

# pede altura e converte para decimal
altura = float(input("Digite sua altura em metros: "))

# pega o ano atual (fixo para iniciante)
ano_atual = 2025

# calcula idade
idade = ano_atual - ano_nascimento

# mostra resultado
print("Olá,", nome, "! Você tem", idade, "anos e sua altura é", altura, "m. Registro concluído.")