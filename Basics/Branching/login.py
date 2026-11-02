uname = "admin"
ps = "12345"

username = input('Enter the username: ')
password = input('Enter the password: ')

if(uname == username and ps == password ):
    print(f'Login Successful')
else:
    print(f'Invalid Credentials')
