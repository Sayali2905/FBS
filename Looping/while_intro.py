# why : to reduce the code redundancy
#what : executes the block of code multiple times 
# when : when the loop execution count is unpredictable 
# how :
# syntax:
#while(condition):
    #block of code

# the block of code will execute till the condition is true when condition become false loop will stop
# while loop can go in infinite loop


#Finite: Variable dependency
    #1. Initialization
    #2. Used in condition
    #3. Value should be changed


i = 0               #Variable initialization
while(i < 5):       #Variable used in condition
    print('Hello World!')    
    i += 1              #Variable value should be change (Increment)