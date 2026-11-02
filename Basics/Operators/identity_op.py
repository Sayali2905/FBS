x = 10    #immutable(integer)   can reuse
y = 10
li1 = [10,20]   #mutable so can't reuse
li2 = [10,20]

#1. is
print(x is y) #checks the memory address  ##True
print(id(x))
print(id(y))
print(li1 is li2)    ##False
print(id(li1))
print(id(li2))

#li1 = (10,20)
#li2 = (10,20)
#tuple so they are also immutable

#2. is not
print(li1 is not li2)       ##True