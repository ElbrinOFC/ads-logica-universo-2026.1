def ler_notas():
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))

    return n1, n2

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_resultado(nome, media, situacao):
    print(f"Nome: {nome}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")

def main():
    nome = input("Digite um nome: ")
    n1, n2 = ler_notas()
    media = calcular_media(n1, n2)
    situacao = verificar_situacao(media)
    resultado = exibir_resultado(nome, media, situacao)
    
main()