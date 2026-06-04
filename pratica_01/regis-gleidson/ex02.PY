# 1. Entrada de dados
v_hora = float(input("Valor por hora: R$ "))
horas = float(input("Total de horas: "))

# 2. Cálculos (Processamento)
bruto = v_hora * horas
imposto = bruto * 0.15
liquido = bruto - imposto

# 3. Exibição dos resultados (Saída)
print("-" * 25)
print(f"VALOR BRUTO:   R$ {bruto:.2f}")
print(f"IMPOSTO (15%): R$ {imposto:.2f}")
print(f"VALOR LÍQUIDO: R$ {liquido:.2f}")
print("-" * 25)