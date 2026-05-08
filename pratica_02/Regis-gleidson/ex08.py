# Solicita o número ao usuário
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\n--- Tabuada do {numero} ---")

# O laço percorre de 1 até 10 (o 11 é o limite exclusivo)
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")