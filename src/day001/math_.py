
# Division is decimal
print(f'5 / 2 = {5 / 2}')

# Round bottom
print(f'5 // 2 = {5 // 2}')

# Round top for negative
print(f'-5 // 2 = {-5 // 2}')

# Workaround
print(f'int(5 / 2) = {int(5 / 2)}')
print(f'int(-5 / 2) = {int(-5 / 2)}')

# Modding
print(f'10 % 3 = {10 % 3}')
print(f'-10 % 3 = {-10 % 3}')

# to be consistent
import math

print(f'math.fmod(-10, 3) = {math.fmod(-10, 3)}')
print(f'math.ceil(10 / 3) = {math.ceil(10 / 3)}')
print(f'math.floor(10 / 3) = {math.floor(10 / 3)}')
print(f'math.pow(10, 3) = {math.pow(10, 3)}')
print(f'math.sqrt(3) = {math.sqrt(3)}')

# Max/min
print(f'Max = {float('infinity')}')
print(f'Min = {float('-infinity')}')

# overflow
# print(f'math.pow(100, 1000) = {math.pow(100, 1000)}')

# no overflow
print(f'100 ** 1000 = {100 ** 1000}')


