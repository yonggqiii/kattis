x, y = float(input()) >= 0, float(input()) >= 0
print((x and y) + 2 * ((not x) and y) + 3 * (not(x or y)) + 4 * (x and (not y)))

