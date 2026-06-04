# Inicializamos o ponto de partida
contador = 10

print("--- Iniciando Contagem Regressiva (while) ---")

# O laço roda enquanto a condição for verdadeira
while contador >= 1:
    print(contador)
    
    # IMPORTANTE: Subtraímos 1 a cada volta para evitar o loop infinito
    contador -= 1

print("Fogo! 🚀")