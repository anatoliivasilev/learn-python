# Разбить ипотечный калькулятор на `read_inputs`, `validate`, `calculate`, `format_result`; `read_inputs`

def read_inputs():
    principal = float(input('Please provide your principal $: '))
    rate = float(input('Please provide your rate %: '))
    years = float(input('Please provide your term (years): '))
    return {
        'principal': principal,
        'rate': rate,
        'years': years
    }

def validate(principal, rate, years):
    if principal <= 0:
        print('Please provide principal > $0')
        return False
    if rate < 0:
        print('Please provide rate >= 0%')
        return False
    if years <= 0:
        print('Please provide term > 0 years')
        return False
    return True

def calculate(principal, rate, years):
    if not validate(principal, rate, years):
        return None
    monthly_rate = rate / 1200
    if rate > 0:
        return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -(years * 12))
    else:
        return principal / (years * 12)

def format_result(result):
    return f'${result:,.2f}'
