def pot(task_integers: list) -> int:
    '''
    https://open.kattis.com/problems/pot
    Define the pot function which solves the problem given a list of
    integers, P1 to PN.

    For example, if the input is 

    1
    212
    1253

    then task_integers would be
    [212, 1253]
    '''
    total = 0
    for integer in task_integers:
        total += int(str(integer)[:-1]) ** int(str(integer)[-1])
    return total

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    print(pot([int(input()) for _ in range(int(input()))]))

if __name__ == '__main__':
    main()

