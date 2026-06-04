# Percorrendo os números de 1 a 20
# O segundo parâmetro do range é exclusivo, por isso usamos 21
for numero in range(1, 21):
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")