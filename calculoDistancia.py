n=float (input('Qual a distância em km que você percorrerá : '))
          
if n>=200:

   preco= n*0.45


else:

   preco=n*0.50

print ('Para a quilometragem desejada {} o valor da passagem será de R$ {:.2f}'.format(n,preco))
