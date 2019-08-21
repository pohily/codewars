

def find_uniq(arr):
    
    if arr[0] != arr[1]:
        if arr[0] != arr[2]:
            return arr[0]
        else:
            return arr[1]
    else:
        ind = 2
        et = arr[0]
        while arr[ind] == et:
            ind += 1
        return arr[ind]


def find_uniq2(arr):
    a, b = set(arr)
    #return a if arr.count(a) == 1 else b
    if arr[0] != arr[1]:
        if arr[0] != arr[2]:
            return a if arr[0] == a else b
        else:
            return a if arr[1] == a else b
    else:
        return b if arr[0] == a else a


