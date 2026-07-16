# Написать `add(a,b)`, `is_even(n)`, `celsius_to_fahrenheit(c)`, `monthly_payment(...)`

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def celsius_to_fahrenheit(c):
    """
    CLI-конвертер Celsius → Fahrenheit.
    (0 °C × 9/5) + 32 = 32 °F
    """
    return c * 9/5 + 32

def monthly_payment(principal, rate, years):
    monthly_rate = rate / 1200
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -(years * 12))

# Для каждой функции записать 2–4 примера вход→выход

print(f'1 + 2 = {add(1, 2)}')
print(f'10 + 6 = {add(10, 6)}')

print(f'11 is even: {is_even(11)}')
print(f'16 is even: {is_even(16)}')

print(f'110°C is {celsius_to_fahrenheit(110)}°F')
print(f'-110°C is {celsius_to_fahrenheit(-110)}°F')

print(f'monthly payment for $500,000 with 4.8% for 25 years is ${monthly_payment(500000, 4.8, 25):,.2f}')
print(f'monthly payment for $500,000 with 0.9% for 25 years is ${monthly_payment(500000, 0.9, 25):,.2f}')

# Показать разницу между `print` и `return`

far = celsius_to_fahrenheit(110)
print(far)


# Функция `max_of_three(a,b,c)` без `max`.
def max_of_three(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


# Функция `count_digits(n)`.
def count_digits(n):
    count = 0
    for i in str(n):
        count += int(i)
    return count

# Функция `is_prime(n)`.
def is_prime(n):
    assert isinstance(n, int), "N should be integer"
    assert n >= 1, "N should be greater than 1"
    assert n <= 1000, "N should be less than 1001"
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
    return result

is_prime(2)
is_prime(1)
is_prime(10001)
is_prime(10.0)
is_prime('test')

