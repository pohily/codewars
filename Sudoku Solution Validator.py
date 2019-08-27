from itertools import chain

def validSolution(board):
    # find subgrids
    subgrids = [[], [], [], [], [], [], [], [], []]
    count = 0
    for subgrid in range(0, 9, 3):
        for subrow in range(0, 9, 3):
            subgrids[count] += board[subgrid][subrow:subrow+3]
            subgrids[count] += board[subgrid+1][subrow:subrow+3]
            subgrids[count] += board[subgrid+2][subrow:subrow+3]
            count += 1
    
    # check all
    to_check = chain(board, zip(*board), subgrids)
    pattern = list(range(1, 10))
    for line in to_check:
        if sorted(line) != pattern:
            return False
    return True

print(validSolution([    [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                         [6, 7, 2, 1, 9, 0, 3, 4, 9],
                         [1, 0, 0, 3, 4, 2, 5, 6, 0],
                         [8, 5, 9, 7, 6, 1, 0, 2, 0],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 0, 1, 5, 3, 7, 2, 1, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 0, 0, 4, 8, 1, 1, 7, 9]]))
