import random

nome  = input("Digite um nome: ")

nome2 =input("Digite um nome: ")

nome3 = input("Digite um nome: ")

nome4 = input("Digite um nome: ")

lista = [nome, nome2, nome3, nome4]

escolhido = random.choice(lista)

print("{} é o escolhido!".format(escolhido))