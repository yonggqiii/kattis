def solve_2048(puzzle: [[int]], move: int) -> [[int]]:
    '''
    https://open.kattis.com/problems/2048
    Define the solve_2048 function which solves the problem given
    the puzzle as a list of lists containing ints, and the move.

    Your function should return the new puzzle after the move.
    The input puzzle must not be amended.
    '''
    pass

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    puzzle = [list(map(lambda x: int(x), input().split(' ')))
            for _ in range(4)]
    move = int(input())
    for row in solve_2048(puzzle, move):
        print(' '.join(map(lambda x: str(x), row)))

if __name__ == '__main__':
    main()

