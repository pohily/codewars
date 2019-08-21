def ordered_count(input):
    used = []
    result = []
    for char in input:
        if char not in used:
            result.append((char, input.count(char)))
            used.append(char)
    return result