tamanho_mb = float(input("Digite o tamanho do arquivo (MB): "))
velociadade_mbps= float(input("Digite  a velocidade da internet (Mbps): "))

tempo_total_segundos = tamanho_mb / (velociadade_mbps / 8)

minutos = int(tempo_total_segundos // 60)
segundos_restantes = int(tempo_total_segundos % 60)

print(f"Tempo estimado de download: {minutos} minutos e {tempo_total_segundos} segundos.")