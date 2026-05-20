# ex06.py
# Escopo basico na pratica

x = 10 # Variável global

def teste():
    y = 5 # Variável local
    return x + y

print(teste())

# Se usar y fora da função, dá esse erro: "NameError: name 'y' is not defined"
# Exemplo feito por mim:
nome = "Carlos"

def mostrar_mensagem():
    mensagem = "Bem-vindo"
    return f"{mensagem}, {nome}"

print(mostrar_mensagem())