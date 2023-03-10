velocidade=float(input('Qual a velocidade média esperada para a viagem em km/h: '))
distancia=float(input('Qual a distancia percorrida em metros: '))

t=distancia/velocidade

print('\nO tempo estimado para a viagem é de: {:.2f} hora(s) e minuto(s)'.format(t))
