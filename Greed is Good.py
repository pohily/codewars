def score(dice):
    result = 0
    for die in range(1, 7):
        if dice.count(die) > 2:
            if die == 1:
                result = 1000
            else:
                result = die * 100
            for i in range(3):
                del dice[dice.index(die)]
            print(dice)
            break
            
    if 1 in dice:
        result += 100
    if 5 in dice:
        result += 50
    return result


print(score([2, 3, 2, 2, 5]))
