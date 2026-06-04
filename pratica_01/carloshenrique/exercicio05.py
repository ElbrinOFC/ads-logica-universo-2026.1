mb = float(input("Digite o tamanho do arquivo (MB): "))
mbps = float(input("Digite a velocidade da internet (Mbps): "))


tempo_segundos = mb / (mbps / 8)


minutos = int(tempo_segundos // 60)
segundos = int(tempo_segundos % 60)


print(f"Tempo estimado de download: {minutos} minutos e {segundos} segundos. ⚡")