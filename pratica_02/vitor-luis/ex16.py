# ex16.py
# Questionário com sentinela

resposta = ""
qtd_sim = 0

while resposta != "FIM":
    resposta = input("Responda S (Sim) ou N (Não) ou FIM (Encerra)")

    if resposta == "S":
        qtd_sim += 1

print(f"Quantidade de SIMs: {qtd_sim}")