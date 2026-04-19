print("Exercício 02")

valor_hora = float(input("Digite o valor por hora: "))
horas = float(input("Digite a quantidade de horas: "))

valor_bruto = valor_hora * horas
imposto = valor_bruto * 0.15
valor_liquido = valor_bruto - imposto

print(f"Valor bruto: R$ {valor_bruto}")
print(f"Imposto (15%): R$ {imposto}")
print(f"Valor líquido: R$ {valor_liquido}")