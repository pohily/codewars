def validBraces(string):
    stack = []
    for char in string:
        if char in '([{':
            stack.append(char)
        if char in ')]}':
            if stack:
                check = stack.pop()
            else:
                return False
            if check == '(' and char == ')':
                continue
            elif check == '[' and char == ']':
                continue
            elif check == '{' and char == '}':
                continue
            else:
                return False
    return False if stack else True


