# Inicializando o acumulador da soma
soma_pares = 0

# Laço para ler 8 números
for i in range(1, 9):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    
    # Filtro de paridade: verifica se o número é par
    if numero % 2 == 0:
        # Se for par, adiciona o valor do número à variável soma_pares
        soma_pares += numero

# Exibindo o resultado final
print(f"\nA soma dos números pares digitados é: {soma_pares}")