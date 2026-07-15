# CLI-конвертер Celsius → Fahrenheit.

def celsius_to_fahrenheit(celsius):
    """
    CLI-конвертер Celsius → Fahrenheit.
    (0 °C × 9/5) + 32 = 32 °F
    """
    return celsius * 9/5 + 32
celsius = float(input('Input temperature °C: ').strip())
fahrenheit = celsius_to_fahrenheit(celsius)
print(f'Temperature in Fahrenheit: {fahrenheit:2} °F')

# CLI-калькулятор чаевых: сумма счёта и процент чаевых.

def bill(sum, tips):
    total = sum * (1 + tips/100)
    print(f'Sum:\t ${sum:,.2f}\nTips:\t {tips:.0f} %\nTotal:\t ${total:,.2f}')
sum = float(input("Input sum in $: ").strip())
tips = float(input("Input tips in %: ").strip())
bill(sum, tips)

# CLI-конвертер секунд в часы/минуты/секунды.

def convert(in_second):
    hours = in_second // 3600
    minutes = (in_second - (hours * 3600)) // 60
    seconds = in_second - (hours * 3600) - (minutes * 60)
    print(f'Hours:\t\t {hours}\nMinutes:\t {minutes}\nSeconds:\t {seconds}')
in_second = int(input('Input seconds: ').strip())
convert(in_second)

# Простой процент: ввести сумму, годовую ставку и число лет; рассчитать только simple interest P*(1+r*t) — формула дана.

def simple_interest(sum, rate, years):
    interest = sum * (1 + rate/100 * years)
    print(f'Sum:\t\t ${sum:,.2f}\nRate:\t\t {rate:.2f}%\nYears:\t\t {years}\nInterest:\t ${interest:,.2f}')

sum = float(input('Enter sum $: ').strip())
rate = float(input('Enter rate %: ').strip())
years = int(input('Enter years: ').strip())
simple_interest(sum, rate, years)


