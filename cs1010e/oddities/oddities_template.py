def oddities(test_cases: [int]) -> [bool]:
    '''
    https://open.kattis.com/problems/oddities
    Define the oddities function which solves the problem given
    a list of test cases.

    Your program should output a list of whether each number is odd
    or not. Odd is True, even is False.

    For example, if test_cases is [1, 2, 3, 4, 5], then your function
    should output [True, False, True, False, True]
    '''
    pass

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    tests = [int(input()) for _ in range(int(input()))]
    res = oddities(tests)
    for i in range(len(tests)):
        print(tests[i], res[i] * 'is odd' + (not res[i]) * 'is even')

if __name__ == '__main__':
    main()

