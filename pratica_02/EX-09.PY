salario = float(input("Digite o salario: "))

if salario <= 1500:
    aumento = salario * 0.15

elif salario > 3000:
    aumento = salario * 0.10

else:
    aumento = salario * 0.05

novo_salario = salario + aumento

print("O novo salario é:", novo_salario)