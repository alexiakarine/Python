salario=float(input('Digite o valor do salário atual: '))
aumento=float(input('Digite a porcentagem de aumento: '))

s=salario+((salario*aumento)/100)

print('O valor do aumento será de {}% e o valor atualizado do salario sera de {:.1f}'.format(aumento,s))


