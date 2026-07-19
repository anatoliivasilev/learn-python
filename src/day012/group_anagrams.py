from collections import defaultdict, deque

# Решить Group Anagrams через `defaultdict(list)`: [задача](https://leetcode.com/problems/group-anagrams/).

class Solution:
    def groupAnagrams(self, strs):
        group = defaultdict(list)
        for str in strs:
            key = sorted(str)
            group[tuple(key)].append(str)
        return list(group.values())

# Реализовать moving average последних k значений через deque.

class MovingAverage:

    def __init__(self, size):
        self.deque = deque()
        self.size = size
        self.total = 0

    def next(self, num):
        self.deque.append(num)
        self.total += num
        if len(self.deque) > self.size:
            k = self.deque.popleft()
            self.total -= k
        return self.total/len(self.deque)

ma = MovingAverage(3)
print(f'ma = MovingAverage(3), {ma}')
print(f'ma.next(1) = {ma.next(1)}')
print(f'ma.next(10) = {ma.next(10)}')
print(f'ma.next(3) = {ma.next(3)}')
print(f'ma.next(5) = {ma.next(5)}')




