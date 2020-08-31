def combine(row: [int]) -> [int]:
    '''
    Combines all equal adjacent pairs.

    For example, combining
     2   2   4   4
           .
           .
    
    [2   2] [4   4]
           .
           .
       
       4       8

    becomes [4, 8]
    '''
    if len(row) <= 1:
        return row
    if row[0] == row[1]:
        return [row[0] + row[1]] + combine(row[2:])
    return [row[0]] + combine(row[1:])

def push_row_left(row: [int]) -> [int]:
    '''
    Push a row to the left.

    For example, if the row is
    2 2 0 4
    Then the result should be
    4 4 0 0
    '''
    # Eliminate all zeroes in the row.
    no_zeroes = [i for i in row if i != 0]

    # Combine all equal adjacent pairs, left associative.
    combined = combine(no_zeroes)

    # Return the result padded with 0s on the right.
    return combined + [0] * (4 - len(combined))

def rotate_left(puzzle: [[int]]) -> [[int]]:
    '''
    Rotates the puzzle 90 degrees to the left.
    '''
    # Start with an empty puzzle.
    res = []

    # Append each element to each new row.
    for i in range(3, -1, -1):
        row = []
        for j in range(4):
            row.append(puzzle[j][i])
        res.append(row)
    return res

def solve_2048(puzzle: [[int]], move: int) -> [[int]]:
    '''
    https://open.kattis.com/problems/2048
    Define the solve_2048 function which solves the problem given
    the puzzle as a list of lists containing ints, and the move.

    Your function should return the new puzzle after the move.
    The input puzzle must not be amended.
    '''
    # Rotate the puzzle 90 degrees to the left by move times.
    for _ in range(move):
        puzzle = rotate_left(puzzle)

    # Push each row left.
    puzzle = [push_row_left(row) for row in puzzle]
    
    # Undo the rotation
    for _ in range(4 - move):
        puzzle = rotate_left(puzzle)

    return puzzle

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    puzzle = [list(map(lambda x: int(x), input().split(' ')))
            for _ in range(4)]
    move = int(input())
    for row in solve_2048(puzzle, move):
        print(' '.join(map(lambda x: str(x), row)))

if __name__ == '__main__':
    main()

