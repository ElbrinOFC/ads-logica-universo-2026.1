soma_dos_pares = 0

for i in range(8):
    numero = int(input("Digite um numero inteiro: "))
    if numero % 2 == 0:
        soma_dos_pares += numero

print("A soma dos numeros pares e: ", soma_dos_pares)