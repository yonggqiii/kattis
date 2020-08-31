def pet(grades: list) -> (int, int):
    '''
    https://open.kattis.com/problems/pet
    Define the pet function which solves the problem given a list
    lists, containing the individual grades for each contestant.

    For example, if the input is
    5 4 4 5
    5 4 4 4
    5 5 4 4
    5 5 5 4
    4 4 4 5

    Then grades will be
    [
        [5, 4, 4, 5],
        [5, 4, 4, 4],
        [5, 5, 4, 4],
        [5, 5, 5, 4],
        [4, 4, 4, 5]
    ]

    Return a tuple in the format of
    (winners_number, points)

    For example, your solution can look like

    # ...
    winners_number = # ...
    # ...
    points = # ...

    return winners_number, points
    '''
    pass

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    winner, points = pet([
        list(map(lambda x: int(x), input().split(' '))) 
        for _ in range(5)
    ])
    print(winner, points)

if __name__ == '__main__':
    main()

