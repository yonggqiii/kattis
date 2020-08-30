res = [sum(map(lambda x: int(x), input().split(' '))) for _ in range(5)]
print(res.index(max(res)) + 1, max(res))
