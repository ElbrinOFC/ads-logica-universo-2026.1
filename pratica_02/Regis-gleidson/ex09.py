# Lendo o salário atual
salario_atual = float(input("Digite o salário atual: R$ "))

# Definindo a lógica de reajuste
if salario_atual <= 1500:
    percentual = 15
elif salario_atual <= 3000:
    percentual = 10
else:
    percentual = 5

# Calculando o aumento e o novo salário
aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + aumento

# Exibindo os resultados
print(f"\n--- Resumo do Reajuste ---")
print(f"Salário antigo: R$ {salario_atual:.2f}")
print(f"Percentual aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")