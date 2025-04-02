maior_valor = lambda x, y: x if x > y else y

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))

print(f"O maior valor é: {maior_valor(num1, num2)}")
