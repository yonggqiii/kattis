for _ in range(int(input())):
    x, y, z = tuple(map(lambda x: int(x), input().split(' ')))
    print('advertise' * (y - z > x) + 'do not advertise' * (x > y - z) + 'does not matter' * (x == y - z))

