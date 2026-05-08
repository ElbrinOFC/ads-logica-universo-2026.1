# Inicializamos a variável com um valor que qualquer nota superaria
maior_nota = -1.0

for i in range(1, 6):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    
    # Se a nota atual for maior que a que temos guardada, ela assume o trono
    if nota > maior_nota:
        maior_nota = nota

print(f"\nA maior nota da turma foi: {maior_nota}")