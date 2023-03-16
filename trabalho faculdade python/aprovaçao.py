def filtrar_aprovados(alunos):
    aprovados = {}
    for nome, nota in alunos.items():
        if nota >= 6.0:
            aprovados[nome] = nota
    return aprovados

alunos = {"João": 8.5, "Maria": 5.0, "Pedro": 7.2, "Lucas": 4.5}
aprovados = filtrar_aprovados(alunos)
print(aprovados)

