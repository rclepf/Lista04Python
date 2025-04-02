def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b if b != 0 else "Indefinida (divisão por zero)"

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

print(f"\nSoma: {somar(num1, num2)}")
print(f"Subtração: {subtrair(num1, num2)}")
print(f"Multiplicação: {multiplicar(num1, num2)}")
print(f"Divisão: {dividir(num1, num2)}")
