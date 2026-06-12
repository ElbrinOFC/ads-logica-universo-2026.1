nota = int(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Nota invalida")
    nota = int(input("Digite uma nota de 0 a 10: "))

    print("Nota valida: ", nota)