total = 0

while True:
    valor = float(input("Digite o valor da compra: R$ "))
    total += valor
    
    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    if continuar == "N":
        break

print(f"\nTotal da compra: R$ {total:.2f}")