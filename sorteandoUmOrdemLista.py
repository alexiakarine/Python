import random

aluno = input("Digite o nome do aluno: ")

aluno1 = input("Digite o nome do aluno: ")

aluno2 = input("Digite o nome do aluno: ")

aluno3 = input("Digite o nome do aluno: ")

lista = [aluno, aluno1, aluno2, aluno3]

random.shuffle(lista)

print("A ordem de apresentação será {}:\n".format(lista))
