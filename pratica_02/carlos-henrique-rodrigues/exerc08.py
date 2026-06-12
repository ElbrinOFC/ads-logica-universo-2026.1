salario = int(input("Digite o salario: R$ "))

if salario <= 1500:
    aumento = salario * 0.15

elif salario <= 3000:
    aumento = salario * 0.10

else: 
    aumento = salario * 0.05

novo_salario = salario + aumento

print("Seu aumento: R$ ", aumento)
print("Novo salario: R$ ", novo_salario)