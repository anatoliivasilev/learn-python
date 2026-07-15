# Ипотечный калькулятор: ввести principal, annual_rate, years;
# отклонить `principal<=0`, `rate<0`, `years<=0`;
# рассчитать monthly payment.

def mortgage_monthly_payment(principal, annual_rate, years):
    if principal <= 0 or annual_rate < 0 or years <= 0:
        print('principal, and years should be > 0, annual_rate should be not < 0')
        return
    elif annual_rate == 0:
        payment = principal / (years * 12)
    else:
        monthly_rate = annual_rate / 12
        payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -(years * 12))
    print(f'Your principal:\t ${principal:,.2f}')
    print(f'Your rate:\t\t {(annual_rate * 100):,.2f}%')
    print(f'Your term:\t\t {years} years')
    print(f'Your payment:\t ${payment:,.2f}')

principal = float(input('Input principal $: ').strip())
annual_rate = float(input('Input annual rate %: ').strip())
years = int(input('Input term in years: ').strip())

mortgage_monthly_payment(principal, annual_rate/100, years)
