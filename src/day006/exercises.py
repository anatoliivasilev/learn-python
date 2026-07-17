# Palindrome без игнорирования punctuation

def palindrome(name):
    return name.lower() == name.lower()[-1::-1]

print(palindrome('Anna'))
print(palindrome('Anatolii'))

# Palindrome с нормализацией через цикл и `isalnum`
def normalize(name):
    normalized = []
    for n in name:
        if n.isalnum():
            normalized.append(n.lower())
    return ''.join(normalized)

print(normalize('AnaTolii Vasilev 124'))

# Run-length encoding `aaabbc -> a3b2c1`
def encode(string):
    last = ''
    result = ''
    count = 0
    for s in string:
        if last == '':
            last = s
            count = 1
            continue
        if last != s:
            result = result + last + str(count)
            count = 1
            last = s
        else:
            count += 1
    return result + last + str(count)

print(encode('aaabbc'))

# Решить [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
def isPalindrome(s: str) -> bool:
    ss = []
    for s1 in s:
        if s1.isalnum():
            ss.append(s1.lower())
    return ''.join(ss) == ''.join(ss[-1::-1])

print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('race a car'))
print(isPalindrome(''))

