'''
Convertion between data types
=============================
    (*) floats can be converted in to: 
            int and vice versa
    (*) string numbers can be converted in to: 
            int and float
'''

mySalary = "73000"
print(type(mySalary)) #<class 'str'>
print(int(mySalary)) #73000
print(type(int(mySalary))) #<class 'int'>

lastWithdraw = "300.50"
print(type(lastWithdraw)) #<class 'str'>
print(float(lastWithdraw)) #300.5
print(type(float(lastWithdraw))) #<class 'float'>