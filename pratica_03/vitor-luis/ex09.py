def dividir(a, b):
    if b == 0:
        return "ERRO: Divisor não pode ser zero"

    return a / b

print(dividir(10, 2))

# Erros:
# * Que erro acontece? o código dá o seguinte erro: "ZeroDivisionError: division by zero"
# * Por que acontece? Python não permite divisão por zero