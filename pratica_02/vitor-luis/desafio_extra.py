# desafio_extra.py
# Sistema simples de lançamento de desempenho

nome = ""
qtd_alunos = 0
total_acertos = 0
media_turma = 0
soma_percentuais = 0

while nome != "sair":
    nome = input("Digite o nome de um estudante (Digite sair caso queira encerrar): ")

    if nome == "sair":
        break

    acertos = int(input("Digite a quantidade de acertos (0 a 20): "))

    if acertos < 0 or acertos > 20:
        print("Erro: Quantidade de acertos inválida")
        acertos = int(input("Digite novamente (0 a 20): "))

    porcentagem = (acertos / 20) * 100

    if porcentagem <= 20:
        print(f"Crítico! Acertos: {porcentagem}%")
    elif porcentagem <= 60:
        print(f"Em atenção! Acertos: {porcentagem}%")
    elif porcentagem <= 80:
        print(f"Satisfatório! Acertos: {porcentagem}%")
    else:
        print(f"Excelente! Acertos: {porcentagem}%")

    soma_percentuais += porcentagem
    qtd_alunos += 1

if qtd_alunos > 0:
    media_turma = soma_percentuais / qtd_alunos
    print(f"Média percentual da turma: {media_turma:.1f}%")
else:
    print("Nenhum estudante foi cadastrado.")