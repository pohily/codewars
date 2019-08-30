def increment_string(strng):
    if not strng:
        return '1'
    if strng.isdigit() and len(strng) == strng.count('9'):
        return str(int(strng) + 1)
    
    count = 0
    while strng[count-1] == '9':
        count -= 1
            
    if strng[count-1].isalpha():
        if not count:
            return strng + '1'
        return strng[:count] + str(int(strng[count:]) + 1)   
    else:
        return strng[:count-1] + str(int(strng[count-1:]) + 1)   

print(increment_string(''))  

'''
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


import re

def increment_string(input):
    match = re.search("(\d*)$", input)
    if match:
        number = match.group(0)
        if number is not "":
            return input[:-len(number)] + str(int(number) + 1).zfill(len(number))
    return input + "1"
    '''       
