def dados_aluno():
    nome = input("Digite o nome do aluno: ")
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))

    return nome, n1, n2

def calc_media(n1, n2):
    return (n1 + n2) / 2

def calc_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Aprovado"

def relatorio(nome, media, situacao):
    print(f"Nome: {nome}")
    print(f"Média: {media}")
    print(f"Situação: {situacao}")

def main():
    nome, n1, n2 = dados_aluno()
    media = calc_media(n1, n2)
    situacao = calc_situacao(media)
    relatorio(nome, media, situacao)

main()