cigarros=int(input('Qual a quantidade de cigarros fumados por dia?: '))
anos=int(input('Quantos anos você já fumou'))

n=anos*365*cigarros*10
tempo=n/(60*24)


print('\nPor conta do cigarro, você ja perdeu: ',tempo)
