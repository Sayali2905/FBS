# for i in range(1,6):
#     for j in range(0,5 - i):
#         print(' ',end = ' ')

#     for k in range(1,2 * i):
#         if(k == 1 or k == 2 * i-1 or i == 5):
#             print('*',end = ' ')
#         else:
#             print(' ',end = ' ')

#     print()

# Universal pattern
row = int(input('Enter the pattern size: '))
for i in range(1,row + 1):
    for j in range(0,row - i):
        print(' ',end = ' ')

    for k in range(1,2 * i):
        if(k == 1 or k == 2 * i-1 or i == row):
            print('*',end = ' ')
        else:
            print(' ',end = ' ')

    print()
