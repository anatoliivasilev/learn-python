# Прочитать строку через input; вывести её тип.
# Преобразовать корректные строки через int() и float(); намеренно получить ValueError на int("abc")
# Отработать + - * / // % **, порядок операций и скобки.
# Вывести деньги через f"{value:.2f}"; сравнить с round(value,2)

inp = input('Input value: ')

iinp = int(inp)
finp = float(inp)

print(inp, iinp)
print(inp, finp)

print(f'{finp} + {finp} =', finp + finp)
print(f'{finp} - {finp} =', finp - finp)
print(f'{finp} / {finp} =', finp / finp)
print(f'{finp} * {finp} =', finp * finp)
print(f'{finp} // {finp} =', finp // finp)
print(f'{finp} % {finp} =', finp % finp)
print(f'{finp} ** 2 =', finp ** 2)

print(f'${finp:.2f}', f'${finp:,.2f}', round(finp, 2))
