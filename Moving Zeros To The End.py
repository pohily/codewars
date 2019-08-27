def move_zeros(array):
    result = []
    zeros = []
    for item in array:
        if item == 0 and not isinstance(item, bool):
            zeros += [0]
        else:
            result.append(item)
    return result + zeros


print(move_zeros([False,1,0,1,2,0,1,3,"a"]))

