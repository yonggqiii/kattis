# Python 3.8+
# print(sum([int((x := input())[:-1]) ** int(x[-1]) for _ in range(int(input()))]))

# Python 3
total = 0
for _ in range(int(input())):
    number = input()
    total += int(number[:-1]) ** int(number[-1])
print(total)
