# Составить таблицу complexity: list index/append/insert/pop(0)/membership; dict/set lookup; sort; slicing.

### List

| Operation  | Complexity   |
|------------|--------------|
| index      | O(1)         |
| append     | O(1) amort   |
| insert     | O(N)         |
| pop        | O(1) amort   |
| membership | O(N)         |
| slice      | O(N)         |
| sort       | O(N * log N) |

### Set/Dict

| Operation  | Complexity |
|------------|------------|
| add        | O(1)       |
| get        | O(1)       |
| membership | O(1)       |

# Для 15 коротких фрагментов определить time/space complexity.

- `x = numbers[0]` - O(1)
- `numbers.append(10)` - O(1)
- `numbers.insert(0, 10)` - O(N)
- `numbers.pop()` - O(1)
- `numbers.pop(0)` - O(N)
- `target in numbers` - O(N)
- `numbers.reverse()` - O(N)
- `copy = numbers[:]` - O(N)

```python
for number in numbers:
    print(number) # O(N)
```
```python
total = 0
for number in numbers:
    total += number # O(N)
```
```python
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(i, j) # O(N2)
```
- `value = user["name"]` - O(1)
- `user["age"] = 30` - O(1)
- `"name" in user` - O(1)
- `unique = set(numbers)` - O(N)

# Проверить `list.pop(0)` против `deque.popleft` на концептуальном уровне
- `list.pop(0)` - O(N) - rebuild all the array
- `deque.popleft` - O(1) - just move the pointer by 1

