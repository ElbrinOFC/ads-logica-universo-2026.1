quantidade = int(input("Quantas notas você quer inserir? "))

soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

media = soma / quantidade

print(f"\nMédia final: {media:.2f}")

if media >= 7:
    print("Aprovado ✅")
elif media >= 5:
    print("Recuperação ⚠️")
else:
    print("Reprovado ❌")
    