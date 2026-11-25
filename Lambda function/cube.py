def cube(n):
    return n ** 3

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = list(map(cube, data))

print(res)