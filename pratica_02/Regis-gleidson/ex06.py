# Solicita a nota pela primeira vez
nota = float(input("Digite uma nota entre 0 e 10: "))

# O laço continua ENQUANTO a nota for menor que 0 OU maior que 10
while nota < 0 or nota > 10:
    print("Valor inválido! A nota deve estar no intervalo de 0 a 10.")
    # Pede a nota novamente para atualizar a condição do loop
    nota = float(input("Por favor, digite uma nota válida: "))

# Exibe a nota aceita pelo sistema
print(f"Nota {nota} registrada com sucesso!")