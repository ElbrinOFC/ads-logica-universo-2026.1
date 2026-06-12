# Inicializando o contador
contador_positivos = 0

# O laço for repetirá a solicitação 10 vezes
for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    
    # Verificando se o número digitado é positivo
    if numero > 0:
        contador_positivos += 1

# Exibindo o resultado final
print(f"\nVocê digitou {contador_positivos} números positivos.")