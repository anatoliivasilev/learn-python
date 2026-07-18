# Создать dict; применить indexing, `get`, update, delete, `items`

d = dict(first=100, second=50, third=200)

print(f'Initial: {d}')

print(f'First: {d.get('first')}')

d.update(first=10)

print(f'after update: {d}')

del d['first']

print(f'After delete: {d}')

print(f'First: {d.items()}')

# Реализовать frequency map вручную.

s = 'Hello, World!'
fm = {}
for l in s:
    c = fm.get(l, 0)
    fm.update({l: c + 1})

print(f'Frequency map: {fm}')

# Создать set; применить add, membership, union, intersection, difference.

cache = {1, 3, 4, 5}

cache.add(1)

cache2 = {2, 6, 7, 4}

if 2 not in cache:
    print(f'2 is not in: {cache}')

print(f'Union: {cache | cache2}')
print(f'Intersection: {cache & cache2}')
print(f'Difference: {cache - cache2}')

# Сравнить поиск элемента в list и set концептуально по сложности.

# list.get()  -> O(N)
# i in set -> O(1)

# Решить [Two Sum](https://leetcode.com/problems/two-sum/) через dict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            if target - num in cache:
                return [cache[target - num], i]
            else:
                cache[num] = i

# Решить [Valid Anagram](https://leetcode.com/problems/valid-anagram/) через frequency map

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fm = {}
        for s1 in s:
            if s1 in fm:
                fm[s1] += 1
            else:
                fm[s1] = 1
        for t1 in t:
            if t1 not in fm:
                return False
            else:
                fm[t1] -= 1
                if fm[t1] == 0:
                    del fm[t1]
        return len(fm) == 0
