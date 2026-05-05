# tamanho do arquivo (MB)
tamanho = float(input("Digite o tamanho do arquivo em MB: "))

# velocidade (Mbps)
velocidade = float(input("Digite a velocidade da internet em Mbps: "))

# converte velocidade (divide por 8)
velocidade_MB = velocidade / 8

# tempo em segundos
tempo_segundos = tamanho / velocidade_MB

# minutos inteiros
minutos = int(tempo_segundos // 60)

# segundos restantes
segundos = int(tempo_segundos % 60)

# resultado final
print(minutos, "minutos e", segundos, "segundos")