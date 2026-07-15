# Упражнение 1: файл выводит визитную карточку из заранее заданных переменных.

name = 'anatolii'
last_name = 'vasilev'
age = 39

print(f'Name:\t\t {name.strip().title()}\nLast Name:\t {last_name.strip().title()}\nAge:\t\t {age} years')

# Упражнение 2: с заранее заданными width=5, height=8 вывести площадь и периметр прямоугольника.

width = 4 #5
height = 34 #8

area = width * height
perimeter = 2 * (width + height)

print(f'Area:\t\t {area}\nPerimeter:\t {perimeter}')

# Упражнение 3: с minutes=135 вывести полные часы и остаток минут, используя // и % после примера из теории.

minutes = 345 #135

hours = minutes // 60
rest = minutes - hours * 60

print(f'Hours:\t\t {hours}\nMinutes:\t {rest}')

# Упражнение 4: изменить значения переменных и повторно запустить файл.

