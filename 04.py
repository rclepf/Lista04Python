def calcular_media(a, b, c):
    return (a + b + c) / 3

valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
valor3 = float(input("Informe o terceiro valor: "))

print(f"A média dos valores informados é: {calcular_media(valor1, valor2, valor3):.2f}")
