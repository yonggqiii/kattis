def circle_estimate(r: float, m: int, c: int) -> (float, float):
    '''
    https://open.kattis.com/problems/estimatingtheareaofacircle
    Define the circle_estimate function which solves the problem
    for a **single** test case given r, m and c.

    Your function should return a tuple in the format of
    (true_area, estimated_area)

    Your program logic can look something like
    # ...
    true_area = # ...
    # ...
    estimated_area = # ...
    # ...
    return true_area, estimated_area
    '''
    pass

### DO NOT EDIT THE PROGRAM BEYOND THIS LINE ###
def main():
    while True:
        i = input()
        if i == '0 0 0':
            break
        line = i.split(' ')
        true_area, estimated_area = circle_estimate(float(line[0]),
                int(line[1]),
                int(line[2]))
        print(true_area, estimated_area)

if __name__ == '__main__':
    main()

