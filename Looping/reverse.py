#wap to reverse a number using while loop
num = int(input("Enter a number: "))    
rev = 0
while(num > 0): 
    d = num % 10
    rev = rev * 10 + d
    num = num // 10
print("Reverse of the number is:", rev)

