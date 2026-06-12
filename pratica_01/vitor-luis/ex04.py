idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite a quantidade de anos de experiência: "))

acesso = (idade >= 18) and (experiencia > 2)

print(f"Acesso Liberado: {acesso}")
