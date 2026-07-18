# Переписать один O(n²) duplicate search через set до O(n)

def duplicate_search(nums): # 0(N2)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def duplicate_search_fixed(nums): # O(N)
    return len(set(nums)) != len(nums)

# Сравнить Two Sum brute force и Hash Map

def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def two_sum_hash_map(nums, target):
    cache = {}
    for i in range(len(nums)):
        if (target - nums[i]) in cache:
            return [cache[target - nums[i]], i]
        else:
            cache[nums[i]] = i
    return None

list, target = [1, 2, 4, 5, 8], 7

print(f'Brute force O(N2): {list}, {target} = {two_sum_brute_force(list, target)}')
print(f'Optimized O(N): {list}, {target} = {two_sum_hash_map(list, target)}')

