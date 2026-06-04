total_fatias = int(input('Informe o total de fatias da pizza: '))
numero_programadores = int(input('Informe o número de programadores: '))

fatias_por_programadores = total_fatias // numero_programadores
sobra = total_fatias % numero_programadores

print(f"Cada programador recebe {fatias_por_programadores} fatias.")
print(f" Sobram {sobra} fatias.")