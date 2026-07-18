for i in range(1,11):
    print(i ** 2)

for i in range(5, 1, -1):
    print(i)

while True:
    i = int(input('input positive number: '))
    if i >= 0:
        break

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
