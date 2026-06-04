# ex07.py
# Soma dos números pares

contador = 0

for i in range(8):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        contador += numero

print(f"{contador}")
