# Definindo a senha correta
senha_correta = "12345678"

# Primeira leitura da senha antes de entrar no laço
entrada = input("Digite a senha para entrar: ")

# O laço continuará repetindo ENQUANTO a entrada for diferente da senha correta
while entrada != senha_correta:
    print("Senha incorreta! Tente novamente.")
    # Leitura da senha dentro do laço (essencial para atualizar a variável)
    entrada = input("Digite a senha: ")

# Esta parte só é executada quando o laço termina (entrada == "acesso")
print("Acesso concedido. Bem-vindo!")