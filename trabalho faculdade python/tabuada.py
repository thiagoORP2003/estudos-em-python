numero = int(input("Digite um número entre 1 e 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Digite um número entre 1 e 10: "))

print("Tabuada do número", numero, ":")
for i in range(1, 11):
    print(numero, "x", i, "=", numero*i)
