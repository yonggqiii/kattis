def favourable(book: list) -> int:
    '''
    https://open.kattis.com/problems/favourable
    Define the favourable function which solves the problem
    given a single book. The function returns the number of
    distinct stories that end in a favourable ending.

    For example, given one particular book as this input:
    4
    1 3 11 13
    3 favourably
    11 catastrophically
    13 favourably

    book will be
    [
        [1, 3, 11, 13],
        [3, 'favourably'],
        [11, 'catastrophically'],
        [13, 'favourably']
    ]
    '''
    pass

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    for _ in range(int(input())):
        print(favourable(
            [list(map(lambda x: x if x == 'favourably' or x == 'catastrophically' else int(x), input().split(' ')))
        for n in range(int(input()))]))

if __name__ == '__main__':
    main()

