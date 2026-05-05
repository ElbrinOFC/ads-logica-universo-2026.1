# total de fatias
total_fatias = int(input("Digite o total de fatias: "))

# número de pessoas
programadores = int(input("Digite o número de programadores: "))

# divisão inteira
fatias_por_pessoa = total_fatias // programadores

# resto da divisão
sobra = total_fatias % programadores

# resultado
print("Cada um come:", fatias_por_pessoa)
print("Sobra:", sobra)