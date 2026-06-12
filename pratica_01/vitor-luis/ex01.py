nome = input("Digite seu nome: ")
ano_nasc = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura (em metros): "))

ano_atual = 2026
idade = ano_atual - ano_nasc

print(
    f"Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído."
)
