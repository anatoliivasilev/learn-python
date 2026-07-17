# Найти min/max/sum вручную циклом

l = [1, 7, 5, 8, 10]

def min(nums):
    min = nums[0]
    for n in nums:
        if n < min:
            min = n
    return min

def max(nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

def sum(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

print(f"""List: {l}
Min: {min(l)}
Max: {max(l)}
Sum: {sum(l)}
""")

# Удалить дубликаты с сохранением порядка пока через второй список.

def remove_duplicates(nums):
    result = []
    cache = set()
    for n in nums:
        if n not in cache:
            result.append(n)
            cache.add(n)
    return result
l.append(5)
print(f'Original: {l}')
print(f'Removed duplicates: {remove_duplicates(l)}')

# Повернуть список вправо на k через slicing
def rotate(k, nums):
    return nums[k:] + nums[:k]

print(f'Original: {l}')
print(f'Rotated: {rotate(3, l)}')

# Объединить два отсортированных списка двумя указателями.

def join_sorted(num1, num2):
    result = []
    i, j = 0, 0
    while i + j < len(num1) + len(num2):
        if i < len(num1) and j < len(num2):
            if num1[i] < num2[j]:
                result.append(num1[i])
                i += 1
            else:
                result.append(num2[j])
                j += 1
        else:
            while i < len(num1):
                result.append(num1[i])
                i += 1
            while j < len(num2):
                result.append(num2[j])
                j += 1
    return result

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6]

print(f'Original 1: {l1}')
print(f'Original 2: {l2}')
print(f'Joined: {join_sorted(l1, l2)}')
print(f'Joined: {join_sorted(l2, l1)}')
