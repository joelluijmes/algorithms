import numpy as np

# function used in asserts to validate argument


def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

# https://stackoverflow.com/questions/16856788/slice-2d-array-into-smaller-2d-arrays

# splits a 2D array into four equal parts, e.g. 8x8 array is splitted in 4 chunks of 4x4
# NOTE: indexing is column first, thus 0 is topleft, 1 is bottomleft, 2 topright, 3 bottomright


def split(arr, nrows, ncols):
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
            .swapaxes(1, 2)
            .reshape(-1, nrows, ncols))


# merges four 2D array chunks into larger, e.g 4 chunks of 4x4 is merged into 8x8
def merge(arr, h, w):
    n, nrows, ncols = arr.shape
    return (arr.reshape(h//nrows, -1, nrows, ncols)
            .swapaxes(1, 2)
            .reshape(h, w))


# draws the board
def draw(board):

    w, h = board.shape
    assert(w == h)
    assert(isPowerOfTwo(w))
    n = w

    for y in range(n):
        for x in range(n):
            if board[x][y] == ' ':
                print(' *', end='')
            else:
                print(' ', end='')
                print(board[x][y], end='')
        print('')


# find the first parent chunk with the gap. Imagine a 8x8 board, and the gap at (x: 3, y: 5)
# - for the large 8x8 board it returns 1 (bottomleft)
# - for the bottom left 4x4 it returns 2 (topright)
# - for the inner top right 2x2 it returns 3 (bottomright)
def find_gap(board):
    w, h = board.shape
    assert(w == h)
    assert(isPowerOfTwo(w))

    def loop(board, index):
        n = board.shape[0]

        if n == 2:
            x, y = np.where(board != ' ')
            if x == 0 and y == 0:
                return 0
            if x == 0 and y == 1:
                return 1
            if x == 1 and y == 0:
                return 2
            if x == 1 and y == 1:
                return 3
            return None

        subsize = n//2
        parts = split(board, subsize, subsize)

        for i in range(4):
            result = loop(parts[i], i)
            if result is not None:
                return i

        return None

    return loop(board, 0)


# fits the chessboard with L-shapes where one tile is filled (the gap.)
def solve(board):
    n = board.shape[0]
    if n == 1:
        return board

    # index is the smaller splitted board where there is a tile filled
    index = find_gap(board)

    subsize = n//2
    parts = split(board, subsize, subsize)

    end = subsize - 1

    # fit a L-shape around the border of the filled tile
    if index == 0:
        parts[1][end][0] = '-'
        parts[2][0][end] = '|'
        parts[3][0][0] = '⌟'
    if index == 1:
        parts[0][end][end] = '-'
        parts[2][0][end] = '⌝'
        parts[3][0][0] = '|'
    if index == 2:
        parts[0][end][0] = '|'
        parts[1][end][0] = '⌞'
        parts[3][0][0] = '-'
    if index == 3:
        parts[0][end][end] = '⌜'
        parts[1][end][0] = '|'
        parts[2][0][end] = '-'

    for i in range(4):
        parts[i] = solve(parts[i])

    return merge(parts, n, n)


# Usage

n = 8

board = np.array([[' ' for x in range(n)] for y in range(n)])
board[3][4] = 'x'

draw(board)

solved = solve(board)
print()
draw(solved)
