# ex15.py
# Maior nota da sequência

maior_nota = 0

for i in range(5):
    nota = float(input(f"Digite a nota {i}: "))

    if nota > maior_nota:
        maior_nota = nota

print(f"{maior_nota}")