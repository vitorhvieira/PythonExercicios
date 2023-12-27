primeiro_nome = input("Digite o primeiro Nome: ")
sobrenome = input("Digite o sobrenome: ")
apelido = input("Digite o apelido: ")


def nome(primeiro_nome, sobrenome, apelido):
    resultado = apelido or (
        f"{primeiro_nome} {sobrenome}" if sobrenome else primeiro_nome
    )
    return print(resultado)


pessoa = nome(primeiro_nome, sobrenome, apelido)
