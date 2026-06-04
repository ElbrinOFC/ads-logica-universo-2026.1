# ex09.py
# Reajuste salarial

salario = float(input("Digite o salário de um funcionário: "))

if salario <= 1500:
    novo_salario = salario + (salario * 0.15)
elif salario > 3000:
    novo_salario = salario + (salario * 0.05)
else:
    novo_salario = salario + (salario * 0.10)

print(f"{novo_salario}")
