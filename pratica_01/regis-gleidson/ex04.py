# 1. Entrada de dados
idade = int(input("Digite sua idade: "))
experiencia = int(input("Anos de experiência: "))

# 2. Lógica Relacional (Sem if/else)
# O Python avalia a expressão e guarda o resultado (True ou False) na variável
acesso_liberado = (idade >= 18) and (experiencia > 2)

# 3. Exibição do resultado
print(f"Acesso Liberado: {acesso_liberado}")