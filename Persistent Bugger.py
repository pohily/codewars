def persistence(n):
    tmp = str(n)
    count = 0
    while len(tmp) > 1:
        result = 1
        for num in tmp:
            result *= int(num)
        tmp = str(result)
        count += 1
    return count