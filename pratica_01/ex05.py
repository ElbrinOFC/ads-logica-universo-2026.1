print("Exercício 05")

tamanho_mb = float(input("Digite o tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (Mbps): "))

# Converter MB para Megabits (1 byte = 8 bits)
tamanho_megabits = tamanho_mb * 8

tempo_total_segundos = tamanho_megabits / velocidade_mbps

minutos = int(tempo_total_segundos // 60)
segundos = int(tempo_total_segundos % 60)

print(f"Tempo estimado: {minutos} minutos e {segundos} segundos.")