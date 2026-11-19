#WAP to check given number by user is armstrong or not
#if yes return True, if no return False

def armstrongNumber(n):

    temp = n
    power = len(str(n))
    sum = 0

    while (temp > 0):
        d = temp % 10
        sum = sum + (d ** power)
        temp = temp // 10

    if(n == sum):
        return True
    else:
        return False

n = int(input('Enter the number: '))

res = armstrongNumber(n)
print(res)