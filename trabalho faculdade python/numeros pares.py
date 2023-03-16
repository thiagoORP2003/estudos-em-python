def retorna_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

# Exemplo de uso da função retorna_pares()
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = retorna_pares(lista_original)
print(lista_pares)  # Saída: [2, 4, 6, 8, 10]
