# Выполнить 15 операций со строкой:
# index, negative index, slices, reverse, lower, upper, strip, split, join, replace, find.

string = 'Hello World! '

idx = string.find('o')
idx2 = string.index('o')
ridx = string.rfind('o')
substring = string[2:8]
revers = string[-1::-1]
low = string.lower()
up = string.upper()
strip = string.strip()
splitted = string.split('o')
string2 = '0'.join(splitted)
replaced = string2.replace('0', 'o')

print(f"""STRING: %s
Find for 'o': %s
Index for 'o': %s
Negative Index for 'o': %s
Slice from 2 to 8: %s
Reversed: %s
Lower: %s
Upper: %s
Stripped: %s
Splitted with 'o': %s
Joined with 0: %s
Replaced with '0' to 'o': %s
""" %
(string, idx, idx2, ridx, substring, revers, low, up, strip, splitted, string2, replaced))

# Попытаться изменить символ по индексу; объяснить `TypeError` и immutable.
# string[2] = 'T'
# Traceback (most recent call last):
# File "/Users/anatoliivasilev/projects/learn-python/src/day006/strings.py", line 34, in <module>
# string[2] = 'T'
# ~~~~~~^^^
# TypeError: 'str' object does not support item assignment

# Написать `normalize_name` и `initials`.

def normalize_name(name):
    chunks = name.split(' ')
    capitalized = []
    for chunk in chunks:
        capitalized.append(chunk.strip().capitalize())
    return ' '.join(capitalized)
print(normalize_name('ANATOLii vAsilev'))

def initials(name):
    chunks = name.split(' ')
    capitalized = []
    for chunk in chunks:
        capitalized.append(chunk.strip().capitalize()[0] + '.')
    return ''.join(capitalized)

# name = input().strip()
print(initials('kRISTINA vAsileva'))

# Написать цикл подсчёта гласных
def vowels(name):
    count = 0
    v = {'o', 'a', 'e', 'i', 'u', 'y'}
    for n in name.lower():
        count += 1 if n in v else 0
    return count

print(vowels('kRISTINA vAsileva'))



