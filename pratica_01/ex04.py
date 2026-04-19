print("Exercício 04")

idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite seus anos de experiência: "))

acesso_liberado = idade >= 18 and experiencia >= 2

print(f"Acesso Liberado: {acesso_liberado}")