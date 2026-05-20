def calcular_media():
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))

    return (n1 + n2) / 2

media = calcular_media()

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

print(verificar_situacao(media))