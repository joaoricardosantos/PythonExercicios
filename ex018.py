import math

angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'SENO {seno:.2f} COSSENO {cos:.2f} TANGENTE {tan:.2f}')