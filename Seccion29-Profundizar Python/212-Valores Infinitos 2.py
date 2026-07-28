#Manejo Valores Infitivo
import math
from decimal import Decimal

infi=float('inf')
# print(f'infinito Posi')
# print(f'Infinito Positvo :{infi}')
# print(f'Es infinito? : {math.isinf(infi)}')

print('\n')

infinito_nega=float('-inf')
# print(f'infinito negativo : {infinito_nega}')
# print(f'Es infinito? : {math.isinf(infinito_nega)}')

print('\n')


infi=math.inf
# print(f'infinito Posi')
# print(f'Infinito Positvo :{infi}')
# print(f'Es infinito? : {math.isinf(infi)}')

print('\n')

infinito_nega=-math.inf
# print(f'infinito negativo : {infinito_nega}')
# print(f'Es infinito? : {math.isinf(infinito_nega)}')
print('\n')


# Modulo DECIMAL
infi=Decimal('Infinity')
print(f'Infinito Positvo :{infi}')
print(f'Es infinito? : {math.isinf(infi)}')

print('\n')


infinito_nega=Decimal('-Infinity')
print(f'infinito negativo : {infinito_nega}')
print(f'Es infinito? : {math.isinf(infinito_nega)}')