def calcular_cobranca():
    valor_por_hora = float(input("Digite o valor por hora (em R$): "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
    taxa_imposto = float(input("Digite a taxa de imposto (em %): "))

    valor_bruto = valor_por_hora * horas_trabalhadas
    impostos = valor_bruto * (taxa_imposto / 100)
    valor_liquido = valor_bruto - impostos

    print(f"\nValor por horas: R$ {valor_por_hora:.2f}")
    print(f"Horas trabalhadas: {horas_trabalhadas}")
    print(f"Valor bruto: R$ {valor_bruto:.2f}")
    print(f"Impostos (R$ {taxa_imposto}%): R$ {impostos:.2f}")
    print(f"Valor líquido: R$ {valor_liquido:.2f}")


if __name__ == "__main__":
    calcular_cobranca()
