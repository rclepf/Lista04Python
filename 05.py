def contar_ate(numero):
    for i in range(1, numero + 1):
        print(i)

num = int(input("Informe um número inteiro positivo: "))

if num > 0:
    contar_ate(num)
else:
    print("Número inválido. Informe um valor maior que zero.")
