def anagrams(word, words):
    etalon = sorted(word)
    result = []
    for check in words:
        if sorted(check) == etalon:
            result.append(check)
    return result