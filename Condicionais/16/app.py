idade_aluno = int(input("Qual idade do aluno?: "))
responsavel = input("Possui um responsavel?: ").lower()


def matricula(idade_aluno, responsavel):
    if idade_aluno < 18:
        idade_aluno = False
    else:
        idade_aluno = True

    if responsavel == "sim":
        responsavel = True
    elif responsavel == "nao":
        responsavel = False

    if idade_aluno and not responsavel:
        return print("Matricula realizada com sucesso!")
    elif not idade_aluno and responsavel:
        return print("Matricula realizade com sucesso!")
    elif idade_aluno and responsavel:
        return print("Matricula realizade com sucesso!")
    else:
        return print("Não é possivel fazer a matricula")


aluno = matricula(idade_aluno, responsavel)
