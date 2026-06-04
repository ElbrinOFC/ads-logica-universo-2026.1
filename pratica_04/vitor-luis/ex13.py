# a) Problema com sort()
# O método sort() organiza a própria lista
# e não retorna uma nova lista
# Por isso, a variável resultado recebe None

lista = [3, 1, 2]
lista.sort()
print(lista)


# b) Problema de índice inexistente
# A lista possui apenas 2 elementos:
# índice 0 -> "Ana"
# índice 1 -> "Bruno"
# O índice 5 não existe, causando IndexError

nomes = ["Ana", "Bruno"]

# Forma segura:
if len(nomes) > 5:
    print(nomes[5])
else:
    print("Índice não existe na lista")


# Desafio opcional
# Exemplo de erro envolvendo strings
# Erro:
# texto = "Python"
# texto[0] = "J"

# Strings são imutáveis em Python
# então não podemos alterar uma letra diretamente

# Correção:
texto = "Python"
novo_texto = "J" + texto[1:]
print(novo_texto)