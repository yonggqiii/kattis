def carrots(n: int, p: int, descriptions: list) -> int:
    '''
    Carrots problem as given in https://open.kattis.com/problems/carrots
    Define the carrots function that solves the problem given n, p
    and the subsequent lines being input to the program.
    '''
    pass

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    n, p = map(lambda x: int(x), input().split(' '))
    print(carrots(n, p, [input() for _ in range(n)]))

if __name__ == '__main__':
    main()

