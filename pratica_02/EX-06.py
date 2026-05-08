nota = float(input("digite uma nota entre 0 e 10:"))

while nota < 0 or nota > 10:
    nota = float(input("nota invalida. digite novamente: "))
    print("nota valida:", nota)