n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i    #sum = sum + i
print(f'Sum of first {n} numbers is: {sum}')



## Dry run

# n      sum    i       sum + i
# 5      0      1       0 + 1 = 1
#        1      2       1 + 2 = 3
#        3      3       3 + 3 = 6
#        6      4       6 + 4 = 10
#        10     5       10 + 5 = 15