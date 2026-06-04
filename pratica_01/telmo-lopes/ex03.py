total_fatias = int(input("Digite o total de fatias: "))
programadores = int(input("Digite o número de programadores: "))

fatias_por_pessoa = total_fatias // programadores
sobra = total_fatias % programadores

print(f"Cada pessoa recebe {fatias_por_pessoa} fatias.")
print(f"Sobram {sobra} fatias na caixa.")