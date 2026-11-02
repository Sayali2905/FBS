# why : to make a decision
# what : where we decide which block of code will execute
# how : when the condition is true if block of code will execute or when the condition is false else block of code will execute

#syntax:
#if(condition):
    #if block of code
#else:
    #else block of code

num = int(input('Enter number:'))
if(num > 0):
    print(f'{num} is positive number.')
else:
    print(f'{num} is a negative number.')