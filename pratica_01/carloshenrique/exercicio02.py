valor_hora = float(input("Digite o valor cobrado por hora: R$ "))
horas = float(input("Digite a quantidade estimada de horas: "))


valor_bruto = valor_hora * horas
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos


print(f"Valor bruto do projeto: R$ {valor_bruto:.2f} 💰")
print(f"Impostos (15%): R$ {impostos:.2f} 💹")
print(f"Valor líquido final: R$ {valor_liquido:.2f} 💸")