print("Exercício 01")

from datetime import datetime

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura em metros: "))

ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

print(f"Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.")