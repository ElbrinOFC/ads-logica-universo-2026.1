print("Exercício 12")

total = 0

while True:
    valor = float(input("Digite o valor da compra: "))
    total += valor

    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar != "S":
        break

print("Total das compras:", total)