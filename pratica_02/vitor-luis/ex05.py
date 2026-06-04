# ex05.py
# Contar números positivos

contador = 0

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero > 0:
        contador += 1

print(f"Quantidade de números positivos: {contador}")
