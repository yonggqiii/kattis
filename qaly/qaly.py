# Python 3.8+
# print(sum([ float((x := input().split(' '))[0]) * float(x[1]) for _ in range(int(input()))]))

# Python 3+
total = 0
for _ in range(int(input())):
    line = input().split(' ')
    total += float(line[0]) * float(line[1])
print(total)
