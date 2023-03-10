produto=float(input('Digite o valor do produto: '))
desconto=float(input('Digite o valor do desconto: '))

valor=(produto-((produto*desconto)/100))

print('\nO valor do desconto foi de R${} e o valor final do produto será: R${} '.format(desconto,valor))
