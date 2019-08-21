def narcissistic( value ):
    tmp = str(value)
    result = 0
    for digit in tmp:
        result += int(digit)**len(tmp)
    return result == value