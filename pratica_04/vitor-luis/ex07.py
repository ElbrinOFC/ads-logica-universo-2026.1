estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

encontrado = False

for i in estudantes:
    if i == procurado:
        encontrado = True
        break

if encontrado:
    print("Nome procurado encontrado!")