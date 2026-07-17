# Найти первый повторяющийся элемент

def first_repeat(nums):
    cache = set()
    for n in nums:
        if n in cache:
            return n
        else:
            cache.add(n)
print(first_repeat([1, 3, 4, 5, 3, 2, 6]))

# Найти общие уникальные элементы двух списков
def unique(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return s1 & s2

print(unique([1, 3, 4, 5, 7, 7, 4], [2, 6, 3, 3, 4, 4]))
