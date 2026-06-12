total_fatias = int(input("Digite o número total de fatias de pizza: "))
programadores = int(input("Digite o número de programadores na equipe: "))


fatias_por_pessoa = total_fatias // programadores
sobra = total_fatias % programadores


print(f"\nCada programador comerá {fatias_por_pessoa} fatias inteiras. 😋")
print(f"Sobrarao {sobra} fatias na caixa. 😨")