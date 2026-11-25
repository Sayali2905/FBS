def sOS(n):
    if(n <= 0):
        return 0
    else:
        return n + sOS(n - 1)

n = 5
res = sOS(n)
print(res)