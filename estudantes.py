ana = estudante("ana")
ana.adicionar_nota(8)
ana.adiocionar_nota(9)
def calcular_media(estudante):
    total = sum(estudante.notas)
    quantidade = len(estudante.notas)
    media = total / quantidade
    return media