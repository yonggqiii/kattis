from math import sin, radians, ceil
x, y = tuple(map(lambda x: int(x), input().split()))
print(ceil(x / sin(radians(y))))
