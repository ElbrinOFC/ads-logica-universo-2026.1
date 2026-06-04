total = 0

while True:
    valor = float(input("Digite o valor da compra: "))
    total += valor

    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar == "N":
        break

print("Total gasto:", total)