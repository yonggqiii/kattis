for _ in range(int(input())):
    b, p = input().split(' ')
    b, p = int(b), float(p)
    print(60 * (b - 1) / p, 60 * b / p, 60 * (b + 1) / p)
