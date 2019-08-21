def tribonacci(signature, n):
    if n < 4:
        return signature[:n]
    result = signature[:]
    for i in range(n - 3):
        result.append(sum(result[-3:]))
    return result  
      