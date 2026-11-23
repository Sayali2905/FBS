###  KEYWORD VARIABLE LENGTH ARGUMENT

def emp(**data):
    #print(data)
    for key, val in data.items():
        print(key, ':', val)

emp(id=101, name='ABC', sal=35000 ,dept='IT')
print('****************************************')
emp(id=102, name='XYZ', sal=45000 ,dept='HR')