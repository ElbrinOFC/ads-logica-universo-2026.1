idade = int(input("Digite a sua idade: "))
experiencia = int(input("Digite os anos de experiência profissional: "))

acesso_liberado = (idade >=18) and (experiencia > 2)

print(f"Acesso Liberado: {acesso_liberado}")