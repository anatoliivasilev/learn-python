# Таблица платежей: для заранее заданного principal
# вывести остаток после 12 одинаковых платежей (без сложных процентов).

def payments(principal, rate, years, payments):
    print(f'Total Sum: ${principal:,.2f}')
    print(f'|{'#':5}|{'Start':12}|{'End':12}|{'Payment':12}|{'Principal':12}|{'Percent':12}|')
    monthly_rate = rate / 12
    payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -(years * 12))
    total = principal
    for i in range(1, payments + 1):
        bank_part = total * monthly_rate
        principal_part = payment - bank_part
        print(f'|{i:5}|{total:12,.2f}|{(total - principal_part):12,.2f}|{payment:12,.2f}|{principal_part:12,.2f}|{bank_part:12,.2f}|')
        total -= principal_part
    print(f'Total Sum after {payments} payments: ${total:,.2f}')

principal = float(input('Input principal $: '))
rate = float(input('Input rate %: '))
years = float(input('Input years: '))
payments(principal, rate/100, years, 60)

# Сумма цифр числа через `while`

inp = input('Input number: ')
total = 0
for i in inp:
    total += int(i)
print(f'Sum is: {total}')

# Проверка простого числа перебором делителей

inp = int(input('Input number: '))
complex = False
for i in range(2, inp):
    if inp % i == 0:
        complex = True
print(f'Is simple: {not complex}')

# Найти максимум в заранее заданной последовательности чисел,
# пока используя список, предоставленный в шаблоне, без методов списка.

sequence = [1,2,4,33,2,43,35]
max = sequence[0]
for n in sequence:
    max = max if max > n else n
print(f'Max is: {max}')

