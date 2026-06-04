opcao = input("Digite C para Celsius → Fahrenheit ou F para Fahrenheit → Celsius: ").upper()

if opcao == "C":
    c = float(input("Digite a temperatura em Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f:.2f}°F")

elif opcao == "F":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c:.2f}°C")

else:
    print("Opção inválida!")