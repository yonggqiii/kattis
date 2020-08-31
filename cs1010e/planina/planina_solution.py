def planina(n: int) -> int:
    '''
    https://open.kattis.com/problems/planina
    Define the planina function which solves the problem given N.
    '''
    return (2 ** n + 1) ** 2

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    print(planina(int(input())))

if __name__ == '__main__':
    main()

