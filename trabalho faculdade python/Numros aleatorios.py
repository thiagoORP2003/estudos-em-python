import random

# Gerando a lista de números aleatórios
numeros = []
for i in range(30):
    numeros.append(random.randint(1, 100))

# Calculando e exibindo a soma, média, máximo e mínimo da lista
soma = sum(numeros)
media = soma / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

print("Lista completa: ", numeros)
print("Soma: ", soma)
print("Média: ", media)
print("Máximo: ", maximo)
print("Mínimo: ", minimo)
