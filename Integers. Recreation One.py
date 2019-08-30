from math import sqrt
def list_squared(m, n):
    result = []
    for number in range(m, n+1):
        divisors = [i for i in range(1, number//2 + 1) if number % i == 0] + [number]
        sum_sq = sum([i**2 for i in divisors])
        x = sqrt(sum_sq)
        if round(x) == x:
            result.append((number, sum_sq))
    return result

print(list_squared(1, 42))
