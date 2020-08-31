def ways_to_get_there(elem: any, prevs: dict, stored: dict) -> int:
    '''
    Use DP to solve problem.
    Ways to get to elem = sum of the ways to get to each of elem's
    previous nodes.
    '''
    if elem == 1:
        return 1
    if elem in stored:
        return stored[elem]

    # Store the result for elem if it has not been computed already.
    stored[elem] = sum([ways_to_get_there(i, prevs, stored) 
        for i in prevs[elem]])
    return stored[elem]

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
    # Build list of previous nodes for each node.
    prevs = {}
    for section in book:
        prev = section[0]
        for next_section in section[1:]:
            if next_section not in prevs:
                prevs[next_section] = []
            prevs[next_section].append(prev)
    
    return 0 \
        if 'favourably' not in prevs \
        else ways_to_get_there('favourably', prevs, {})

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    for _ in range(int(input())):
        print(favourable(
            [list(map(lambda x: x if x == 'favourably' or x == 'catastrophically' else int(x), input().split(' ')))
        for n in range(int(input()))]))

if __name__ == '__main__':
    main()

