side_length, x, y = tuple(map(lambda x: int(x), input().split(' ')))
print(4 * max(side_length - x, x) * max(side_length - y, y))
