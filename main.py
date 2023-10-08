
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def printBoard(board, rowValues, colValues):
    for i in range(board[0].size()):
        print(board[i])



if __name__ == '__main__':
    size = 10
    rowValues = [[1, 1], [1, 2, 1], [2, 2, 1], [1, 2, 1], [1, 1, 1], [1, 6], [2, 3, 1], [2, 6], [8], [8]]
    colValues = [[3], [1, 4], [4, 2], [1, 1, 2], [3, 5], [9], [5], [1, 3], [10], [1]]

    board = [[0 for c in range(size)] for r in range(size)]

    for i in range(size):
        print(board[i])

