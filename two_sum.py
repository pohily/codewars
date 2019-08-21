def two_sum(numbers, target):
    for i1, v1 in enumerate(numbers):
        for i2, v2 in enumerate(numbers):
            if v1 != v2 and v1 + v2 == target:
                return [i1, i2]
            elif v1 == v2 and i1 != i2 and v1 + v2 == target:
                return [i1, i2]