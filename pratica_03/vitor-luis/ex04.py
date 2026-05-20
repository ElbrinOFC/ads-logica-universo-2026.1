def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

media = calcular_media(8, 6)

print(f"Média: {media:.1f}")
print(verificar_situacao(media))