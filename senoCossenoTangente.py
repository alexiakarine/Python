import math
angulo = float(input("Digite o ângulo desejado: "))

cos =  math.cos(math.radians(angulo))

sen = math.sin(math.radians(angulo))

tang = math.tan(math.radians(angulo))

print(f"Segundo o ângulo {angulo}, o seno é {sen}")

print(f"Segundo o ângulo {angulo}, cosseno{cos}")

print(f"Segundo o ângulo {angulo}, a tangente é {tang}")

#ou

#from math import radians, sin, cos, tan
#
#cos = cos(radians(angulo))
#
#sen = sin(radians(angulo))
#
#tang = tan(radians(angulo))
