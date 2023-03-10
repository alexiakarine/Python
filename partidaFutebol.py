#Alexia e bruna exercicio1
visitante=str(input('\n\nDigite o nome do time visitante: '))
timedacasa=str(input('\n\nDigite o nome do time da casa: '))
gols1=int(input('\n\nDigite quantos gols o visitante fez: '))
gols2=int(input('\n\nDigite quantos gols o time da casa fez: '))

if(gols1>gols2):

    print('\nVitória dos visitantes !!!')

if(gols2>gols1):
    
    print('\nVitória do time da casa !!! ')


else:
    print('\nEmpate')
