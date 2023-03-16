frase = input("Digite uma frase: ").lower()
frequencia_letras = {}

for letra in frase:
    if letra.isalpha():
        if letra in frequencia_letras:
            frequencia_letras[letra] += 1
        else:
            frequencia_letras[letra] = 1

print("Frequência de cada letra na frase:")
for letra, frequencia in frequencia_letras.items():
    print(letra, "=", frequencia)
