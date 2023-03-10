largura = float(input("Digite a largura da parede: "))

altura = float(input("Digite a altura da parede: "))

area = largura * altura

litros = area / 2

print(f"Sua parede com dimensão de {largura} x {altura} possui uma área de {area}m², "
      f"portanto será necessário {litros} litros de tinta")
