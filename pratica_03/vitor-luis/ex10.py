# ex10.py
# Teste de mesa + caso de teste

def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

print(calcular_total(50, 2))

# Parte A - Teste de mesa

# Chamada:
# calcular_total(50, 2)
# | preco | quantidade | subtotal | desconto | total |
# |  50   |      2     |    100   |    10    |   90  |
#
# calcular_total(100, 5)
# | preco | quantidade | subtotal | desconto | total |
# |  100  |      5     |    500   |    50    |  450  |
#
# calcular_total(0, 1)
# | preco | quantidade | subtotal | desconto | total |
# |   0   |      1     |     0    |     0    |   0   |
#
# calcular_total(1000000, 1000)
# | preco | quantidade | subtotal | desconto |  total   | 
# |1000000|    1000    |1000000000| 100000000|900000000 |

# Parte B - Casos de teste

# Caso normal
# calcular_total(50, 2)
# Resultado esperado: 90.0

# Caso normal
# calcular_total(100, 5)
# Resultado esperado: 450.0

# Caso limítrofe
# calcular_total(0, 1)
# Resultado esperado: 0.0

# Caso extremo
# calcular_total(1000000, 1000)
# Resultado esperado: 900000000.0