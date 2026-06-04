print("Exercício 9")

salario = float(input("Digite o salário: "))

if salario <= 1500:
    aumento = salario * 0.15
elif salario <= 3000:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

print("Novo salário:", salario + aumento)