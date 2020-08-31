def qaly(periods_of_life: list) -> float:
    '''
    https://open.kattis.com/problems/qaly
    Define the qaly function which takes in a list of lists,
    each containing q and y.
    For example, if the input is
    
    2
    1.0 2.0
    3.0 4.0

    then periods_of_life would be
    [[1.0, 2.0], [3.0, 4.0]]
    '''
    total = 0
    for period in periods_of_life:
        total += period[0] * period[1]
    return total

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    print(qaly([list(map(lambda x: float(x), input().split(' ')))
            for _ in range(int(input()))]))

if __name__ == '__main__':
    main()

