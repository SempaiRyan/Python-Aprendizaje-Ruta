import math

from decimal import Decimal

# NaN= Not a Number (No es un numero)
# No es sencible a mayus/minus
a=float('NaN')
# print(f'a : {a}')
#
# print(f'Na (not a number) ? : {math.isnan(a)}')


a=Decimal('NaN')
print(f'a : {a}')
print(f'Na (not a number) ? : {math.isnan(a)}')
