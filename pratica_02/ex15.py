print("Exercício 15")

maior = float('-inf')

for i in range(5):
    nota = float(input("Digite a nota: "))
    if nota > maior:
        maior = nota

print("Maior nota:", maior)