# Lendo o número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verificando as condições
if numero > 0:
    print(f"O número {numero} é Positivo.")
elif numero < 0:
    print(f"O número {numero} é Negativo.")
else:
    print("O número é Zero.")