#logical operators : works on multiple conditions

#1. and: If both operands are True then return True,otherwise return False

print(True and True)  ## True

#2. or: If both operands are False then return False,otherwise True
print(False or False)  ## False
print(True or False)   ## True

#3. not: Opposite of operands
print(not True)        ## False
print(not False)       ## True



#op1        op2          and         or
#True       True         True        True
#True       False        False       True
#False      True         False       True
#False      False        False       False