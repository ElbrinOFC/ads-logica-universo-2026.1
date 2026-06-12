# ex02.py
# Classficação por idade

idade = int(input("Digite uma idade: "))

if idade < 18:
    print("Menor de idade")
elif idade >= 60:
    print("Idoso")
else:
    print("Maior de idade")
