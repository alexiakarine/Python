dia=int(input('Digite a quantidade de dias: '))
horas=int(input('\nDigite a qauntidade de horas: '))
minutos=int(input('\nDigite a quantidade de minutos: '))
segundos=int(input('\nDigite a quantidade de segundos: '))

d=(dia*24)
d1=(d*3600)
h=(horas*3600)
m=(minutos*60)

calculo=(d1+h+m+segundos)

print('\nO total dos valores digitados são em segundos: ',calculo)
