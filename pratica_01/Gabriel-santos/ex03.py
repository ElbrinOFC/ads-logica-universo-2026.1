total_fatias = int(input("Digite o numero total de fatias de pizza: "))
num_programadores = int(input("Digite o número de programadores na equipe: "))

fatias_por_pessoa = total_fatias // num_programadores
sobras = total_fatias % num_programadores

print("-" * 30)
print(f"Cada programador receberá {fatias_por_pessoa} fatias inteiras.")
print(f"Sobra(m) {sobras} fatias(s) na caixa.")
print("-" * 30)