participantes = [
    {"nome": "João"},
    {"nome": "Ana"},
    {"nome": "Beatriz"},
    {"nome": "Maria"},
    {"nome": "Ana Clara"},
    {"nome": "Joana"},
    {"nome": "Augusto"},
    {"nome": "Renan"},
    {"nome": "Patricia"},
    {"nome": "Carlos"},
    {"nome": "Renato"},
    {"nome": "José"},
    {"nome": "Roberto"},
    {"nome": "Sara"},
    {"nome": "Junior"},
    {"nome": "Pedro"},
    {"nome": "Vitor"},
    {"nome": "Antonio"},
]
index = None
for i, pessoa in enumerate(participantes):
    if pessoa["nome"] == "Carlos":
        index = i + 1
        break

if index is not None:
    print(f"Galera... O Carlos está na posição {index}, corre lá!")
else:
    print("O Carlos não está na festa.")
