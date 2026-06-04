tamanho_mb = int(input("Digite o tamanho do arquivo em Megabytes (MB): "))
velocidade_mbps = int(
    input("Digite a velocidade da internet em Megabits por segundo (Mbps): ")
)

tempo_segundos = tamanho_mb / (velocidade_mbps / 8)
minutos_inteiros = int(tempo_segundos // 60)
segundos_restantes = int(tempo_segundos % 60)

print(f"{minutos_inteiros} minutos e {segundos_restantes} segundos")
