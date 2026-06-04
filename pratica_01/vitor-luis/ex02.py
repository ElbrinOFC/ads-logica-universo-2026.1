valor_hora = float(input("Digite o valor cobrado por hora: "))
horas = int(input("Digite a estimativa de horas para conclusão: "))

valor_bruto = horas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print(f"Valor bruto: {valor_bruto}")
print(f"Valor dos impostos: {impostos}")
print(f"Valor líquido final: {valor_liquido}")
