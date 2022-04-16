'''
Operators in Python
=====================================================
    • Arithmetic Operators 
    • Assignment Operators 
    • Comparison Operators 
    • Logical Operators 
    • Identity Operators 
    • Membership Operators 
    • Bitwise Operator
'''

'''
Arithmetic Operators 
=====================================================
    (*) a + b
    (*) a - b
    (*) a * b
    (*) a / b

    (*) a % b       : modulus
    (*) a ** b      : exponential   
    (*) a // b      : floor division
'''

x = 5
y = 2

print(x % y) 
# Devide and give remainder
# output: 1
print(x ** y) 
# same as 2*2*2*2*2 
# output: 32

'''
the floor division 'rounds the result down' to the 'nearest whole number'
'''

x = 15
y = 2
print(x // y) 
# 15/2 = 7.5 but when round down
# output: 7

'''
Assignment Operators 
=====================================================
    (*) a = “String” 
    (*) a += 10 
    (*) a -= 10 
    (*) a *= 10 
    (*) a /= 10 
    (*) a %= 10 
    (*) a **= 2 
    (*) a //= 10
'''

'''
Comparison Operators: returns either True or False
=====================================================
    (*) a == b 
    (*) a != b 
    (*) a > b 
    (*) a < b 
    (*) a >= b 
    (*) a <= b
'''

'''
Logical Operators
=====================================================
    (*) not (a<10)          : returun the opposite
    (*) (a<10) and (b<15)   : true if both are true
    (*) (a<10) or (b<15)    : false if both are false
'''

'''
Identity Operators
=====================================================
    (*) is      : 
                - True if the operands are identical (refer to the same object)
                - True if both values are same
    (*) is not  : 
                - True if the operands are not identical (do not refer to the same object)
                - True if both values are not same
'''
var1 = "Hello"
var2 = "Hello"
print(var1 is var2) #True

var1 = "Hello1"
var2 = "Hello2"
print(var1 is var2) #False

'''
Dictionary in Python (for membership operators)
=====================================================
'''

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car["model"]
print(x)

'''
Membership Operators
=====================================================
    (*) in      : True if value/variable is found in the sequence
    (*) not in  : True if value/variable is not found in the sequence

    Test for a value in a sequence: string, list, tuples 
        (*) also dictronaries
'''

x = 'Hello world'
y = {1:'a',2:'b'}

print('H' in x) # True
print('Hello' in x) # True
print('h' in x) # case sensitive, so False
print(1 in y) # check only keys, so True
print('a' in y) # check only keys, so False

'''
Bitwise Operators
    • Compares bits (1 and 0) 
    • The result is a bit: 1 or 0
=====================================================
    (*) a & b       : 1 if both are 1
    (*) a | b       : 0 if both are 0
    (*) ~ a         : ~x = -(x+1)
                    : for example ~5 = -6
    (*) a ^ b       : XOR (1 if inputs are different)
    (*) a << 2      : 
    (*) a >> 2      :
'''

print(0 & 0) # output: 0
print(0 & 1) # output: 0
print(1 & 0) # output: 0
print(1 & 1) # output: 1

print(0 | 0) # output: 0
print(0 | 1) # output: 1
print(1 | 0) # output: 1
print(1 | 1) # output: 1

print(~1) # output: -(1+1) = -2
print(~2) # output: -(2+1) = -3
print(~3) # output: -(3+1) = -4
print(~4) # output: -(4+1) = -5
print(~5) # output: -(5+1) = -6
print(~6) # output: -(6+1) = -7
print(~7) # output: -(7+1) = -8
print(~8) # output: -(8+1) = -9
print(~9) # output: -(9+1) = -10

print(~-1) # output: -(-1+1) = 0
print(~-2) # output: -(-2+1) = 1
print(~-3) # output: -(-3+1) = 2
print(~-4) # output: -(-4+1) = 3
print(~-5) # output: -(-5+1) = 4
print(~-6) # output: -(-6+1) = 5
print(~-7) # output: -(-7+1) = 6
print(~-8) # output: -(-8+1) = 7
print(~-9) # output: -(-9+1) = 8

print(~-0) # output: -(-0+1) = -1
print(~0) # output: -(0+1) = -1

print(0 ^ 0) # output: 0
print(0 ^ 1) # output: 1
print(1 ^ 0) # output: 1
print(1 ^ 1) # output: 0

print(10 << 2)
'''
first convert 10 into binary
then shift 2 bits left (add 2 zeros to the end)
then convert the result into decimal

1010 
101000 = 40
'''

print(10 >> 2)
'''
first convert 10 into binary
then shift 2 bits right (remove 2 digits from front)
then convert the result into decimal

1010 
10 = 2
'''