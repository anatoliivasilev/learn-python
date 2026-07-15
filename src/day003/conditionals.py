# Проверить операторы `== != < <= > >=`; записать 8 примеров.
a = int(input('Input a: ').strip())
b = int(input('Input b: ').strip())

print(f'{a} == {b}', a == b)
print(f'{a} != {b}', a != b)
print(f'{a} < {b}', a < b)
print(f'{a} <= {b}', a <= b)
print(f'{a} > {b}', a > b)
print(f'{a} >= {b}', a >= b)

# Написать ветвление для negative/zero/positive

if a < b:
    print('a is less than b')
elif a > b:
    print('a is greater than b')
else:
    print('a equals b')

# Калькулятор тарифа доставки по сумме заказа и статусу premium
def tariff_calc(sum, status):
    additional = 5
    if sum < 30:
        additional += 5
    elif sum > 150:
        additional += additional * 0.05
    if status == 'premium':
        additional /= 2
    return sum + additional
print(tariff_calc(100, 'premium'))

# Определение високосного года.

def leap_year(year):
    return True if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else False

print(leap_year(1200), leap_year(1204), leap_year(1205), leap_year(1100))
