from string import ascii_lowercase

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

print(is_pangram("abcdefghijklmopqrstuvwxyz"))
