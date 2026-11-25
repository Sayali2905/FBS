#WAP to print 1-10 

def num(i):
    if(i > 10):
        return
    print(i)
    num(i + 1)

num(1)