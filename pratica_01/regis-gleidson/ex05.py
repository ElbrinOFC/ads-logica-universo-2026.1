# 1. Entrada de dados
tamanho_mb = float(input("Tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Velocidade da internet (Mbps): "))

# 2. Cálculos
# Primeiro, convertemos a velocidade de bits para Bytes (dividindo por 8)
# Depois, dividimos o tamanho do arquivo por essa velocidade real
tempo_total_segundos = tamanho_mb / (velocidade_mbps / 8)

# Convertendo para minutos e segundos usando divisão inteira e módulo
minutos = int(tempo_total_segundos // 60)
segundos = int(tempo_total_segundos % 60)

# 3. Exibição do resultado
print("-" * 30)
print(f"Tempo estimado: {minutos} minutos e {segundos} segundos")
print("-" * 30)