aluno = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota do aluno {}: ".format(aluno)))

nota2 = float(input("Digite a segunda nota do aluno {}: ".format(aluno)))

media = (nota1 + nota2)/2

if media<5:
    print("{} está reprovado com média igual a {} ".format(aluno, media))

elif media == 5:
    print("{} está em exame com média igual a {} ".format(aluno, media))

else:
    print("{} está aprovado com média igual a {} ".format(aluno, media))

