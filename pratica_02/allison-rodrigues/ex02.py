# valor por hora
valor_hora = float(input("Digite o valor por hora: "))

# horas trabalhadas
horas = float(input("Digite a quantidade de horas: "))

# cálculo do valor bruto
valor_bruto = horas * valor_hora

# cálculo do imposto (15%)
impostos = valor_bruto * 0.15

# valor final
valor_liquido = valor_bruto - impostos

# exibe resultados
print("Valor bruto:", valor_bruto)
print("Impostos:", impostos)
print("Valor líquido:", valor_liquido)