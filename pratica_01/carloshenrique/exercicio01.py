from datetime import datetime


nome = input("Qual o seu nome?")
ano_nascimento = int(input("Qual o ano do seu nascimento?"))
altura = float(input("Qual sua altura?"))

ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento


print(f"Olá, {nome}! Voce tem {idade} anos e sua altura é {altura}m. Registro concluído.")