#write a program to write a multiplication table of a given number
num = int(input('Enter the number:'))

i = 1
while(i <= 10):
    mul = num * i
    print(f'{num} * {i} = {mul}')
    i += 1