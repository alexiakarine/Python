import math

catetoO = float(input("Qual o comprimento do cateto oposto? "))

catetoA = float(input("Qual o comprimento do cateto adjascente? "))

hipo = math.hypot(catetoA, catetoO)

print(f"A hipotenusa vai medir {hipo:.2f}")


'''catetoO = float(input("Qual o comprimento do cateto oposto? "))

catetoA = float(input("Qual o comprimento do cateto adjascente? "))

hipotenusa = ((catetoA ** 2) + (catetoO ** 2 )) ** (1/2)

print(f"A hipotenusa vai medir {hipotenusa}")'''
