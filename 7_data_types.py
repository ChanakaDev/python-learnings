'''
=============================
type() function
=============================
- obtain data type of a variable: use type() function
- output gives as a class
    (*) <class 'str'>
    (*) <class 'int'>
    (*) <class 'float'>

=============================
Python primitive data types: 
=============================
    (*) numeric
    (*) text
    (*) boolean 

Numeric data types:
----------------------
    (*) int     = negative & positive numbers
    (*) float   = decimals, scientific, exponential
    (*) complex = with imaginary parts (j)

Represent strings(text):
----------------------
    (*) using ''        : single line
    (*) using ""        : single line
    (*) using \         : multi line # this make multiple lines a one line of text
    (*) using """ """   : multi line # this output the text as it is there

Boolean data type:
----------------------
    (*) bool(0)         : False
    (*) bool("")        : False
    (*) bool([])        : False
    (*) bool(None)      : False
'''

name = "Falan Andria"
print(type(name)) #<class 'str'>

age = 24
print(type(age)) #<class 'int'>

price = 4275.43
print(type(price)) #<class 'float'>

multiLineStr1 = 'this '\
    'is '\
    'an '\
    'example'

print(multiLineStr1) #this is an example

multiLineStr2 = """
                this 
                is 
                an 
                example
                """

print(multiLineStr2)

'''
output:
                this 
                is 
                an 
                example
'''

print(bool(0)) #False
print(bool("")) #False
print(bool([])) #False
print(bool(None)) #False