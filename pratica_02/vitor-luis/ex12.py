# ex12.py
# Classificação de compras

continuar = "S"

while continuar == "S":
    valor = int(input("Digite o valor da compra: "))

    if valor <= 100:
        print("Sem desconto")
    elif valor <= 200:
        print("Desconto básico")
    else:
        print("Desconto especial")

    continuar = input("Deseja continuar? ")
