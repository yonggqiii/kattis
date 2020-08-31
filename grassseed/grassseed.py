c, l = float(input()), int(input())
total = 0
for _ in range(l):
    w, h = input().split(' ')
    total += c * float(w) * float(h)
print(total)

