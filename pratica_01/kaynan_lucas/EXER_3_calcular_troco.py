valor = float(input("Digite o valor da compra: R$ "))
pago = float(input("Digite o valor pago: R$ "))

troco = pago - valor

if troco < 0:
    print("Valor insuficiente! ❌")
else:
    print(f"Troco: R$ {troco:.2f} 💵")