n=int (input('Digite a velocidade do carro em km/h : '))
          
if n>80:
   v=n-80
   m=v*7

   print ('você ultrapassou a velocidade permitida, deve pagar uma multa de: R$ {:.2f}'.format (m))

else:
   print ('Parabéns você está dentro do limite de velocidade, continue assim !! ')
