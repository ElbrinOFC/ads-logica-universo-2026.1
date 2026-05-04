# 1. Entrada de dados
total_fatias = int(input("Total de fatias de Bolo: "))
num_pessoas = int(input("Número de Pessoas: "))

# 2. Cálculos (Processamento)
# // faz a divisão inteira (descarta os decimais)
fatias_por_pessoa = total_fatias // num_pessoas

# % calcula o resto da divisão (o que sobra na caixa)
sobra = total_fatias % num_pessoas

# 3. Exibição dos resultados (Saída)
print("-" * 30)
print(f"Cada pessoa comerá: {fatias_por_pessoa} fatias")
print(f"Sobra na caixa: {sobra} fatias")
print("-" * 30)