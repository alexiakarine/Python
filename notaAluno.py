vnota1=int(input('Digite a nota 1: '))
vnota2=int(input('Digite a nota 2: '))
vnota3=int(input('Digite a nota 3: '))

vmedia=(vnota1+vnota2+vnota3)/3
print(vmedia)

if vmedia>6:
    print('Aprovado')

elif vmedia<4:
    print('Reprovado')

else:
    print('Recuperação')
