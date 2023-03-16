def retorna_strings_longas_com_a(lista):
    longas_com_a = []
    for palavra in lista:
        if len(palavra) > 5 and 'a' in palavra:
            longas_com_a.append(palavra)
    return longas_com_a

lista_original = ["casa", "mochila", "carro", "banana", "cadeira"]
lista_longas_com_a = retorna_strings_longas_com_a(lista_original)
print(lista_longas_com_a)  # Saída: ['mochila', 'banana', 'cadeira']
