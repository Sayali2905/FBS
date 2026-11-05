#Range function:
#why: it generates values effortlessly 
#range(start, stop, step)
#if we dont provide step, it will take default value as 1.
#range(1, 11 , 1)       # 1 to 10
#range(1, 10 , 2)       # 1, 3, 5, 7, 9
#multiplication table of 2
#range(2, 21, 2)       # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
#multiplication table of 5
#range(5, 51, 5)       # 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
#multiplication table of n
#range(n, n*11, n)       # n, 2n, 3n, 4n, 5n, 6n, 7n, 8n, 9n, 10n
#range(n, n*10+1, n)       # n, 2n, 3n, 4n, 5n, 6n, 7n, 8n, 9n, 10n
#multiplication table in reverse order
#range(n*10, n-1, -n)       # 10n, 9n, 8n, 7n, 6n, 5n, 4n, 3n, 2n, n


#for i in range(1, 11, 1):
#for i in range(2, 21, 2):
#for i in range(5, 51, 5):

n = 19
#for i in range(n, n*10+1, n):
#for i in range(n*10, n-1, -n):

#for i in range(1,101):
#for i in range(5):
#if we dont provide start and stop values, it will take default values as 0 and 1 respectively.
#    print(i)

#sum of first n numbers.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i    #sum = sum + i
print(f'Sum of first {n} numbers is: {sum}')
