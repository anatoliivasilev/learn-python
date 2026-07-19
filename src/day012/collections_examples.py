from collections import Counter, defaultdict, deque

# Переписать frequency map через `Counter`
def frequency_map(word):
    cache = {}
    for letter in word.strip().lower():
        cache[letter] = cache.setdefault(letter, 0) + 1
    return cache

def frequency_map_new(word):
    counter = Counter(word.strip().lower())
    return dict(counter)

print(f'old frequency map: {frequency_map('Hello, world!')}')
print(f'new frequency map: {frequency_map_new('Hello, world!')}')

# Построить grouping через `defaultdict(list)`.
def frequency_map_defaultdict(word):
    cache = defaultdict(int)
    for letter in word.strip().lower():
        cache[letter] = cache[letter] + 1
    return dict(cache)

print(f'frequency map (defaultdict): {frequency_map_defaultdict('Hello, world!')}')

# Реализовать FIFO queue через `deque`; применить append/popleft

d = deque()

print(f'deque = {d}')
d.append(1)
d.append(2)
print(f'deque = {d}')
first = d.popleft()
print(f'first = {first}, deque = {d}')

# Сравнить обычный dict и defaultdict в adjacency-list skeleton.

chain = [1, 2, 3, 4, 5]
d1 = dict()
d2 = defaultdict(list)

print(f'---\nlist = {chain}\ndict = {d1}\ndefaultdict = {d2}\n---')

for n in chain:
    d1[n] = d1.setdefault(n, [])
    d1[n].append(n)
    d2[n].append(n)

print(f'---\nlist = {chain}\ndict = {d1}\ndefaultdict = {dict(d2)}\n---')





