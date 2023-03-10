km=float(input('Qual foi a quantidade de quilometros percorridos? :'))
dia=int(input('Qual a quantidade de dias o carro ficou alugado?: '))

valor=((km*0.15)+(dia*60))

print('\nO valor a ser pago pelo pacote de aluguel é:{:.2f}'.format(valor))
