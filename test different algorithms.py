from string import ascii_lowercase
import time


def is_pangram(s):
    count = {}
    for letter in ascii_lowercase:
        count[letter] = 0
    for letter in s:
        if not letter.isalpha():
            continue
        count[letter.lower()] += 1
    print(count)
    return not 0 in count.values()

def is_pangram2(s):
    return set(ascii_lowercase) <= set(s.lower())



t0 = time.time()
print('1', is_pangram("The quick brown fox jumps over the lazy dog"))
elapsed = time.time() - t0

t1 = time.time()
print('2', is_pangram2("The quick brown fox jumps over the lazy dog"))
elapsed2 = time.time() - t1

print(elapsed, elapsed2)
