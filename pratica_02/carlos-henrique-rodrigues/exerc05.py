contador_positivos = 0 

for i in range(10):
    numero = int(input("Digite um numero: "))

    if numero > 0:
        contador_positivos += 1

        print("Quantidade de numeros positivos: ", contador_positivos)