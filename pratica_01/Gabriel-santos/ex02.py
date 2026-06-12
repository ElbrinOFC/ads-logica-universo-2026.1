valor_hora = float(input("Digite o valor cobrado por hora: "))
horas_estimadas = float(input("Digite a estimativa de horas para o projeto: "))

valor_bruto = valor_hora * horas_estimadas
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print("-" * 30)
print(f"valor Bruto: R$ {valor_bruto:.2f}")
print(f"Valor dos Impostos (15%): R$ {impostos:.2f}")
print(f"Valor Líquido Final: R$ {valor_liquido:.2f}")
print("-" * 30)