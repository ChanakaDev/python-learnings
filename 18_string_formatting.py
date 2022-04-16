# *********************************
# Using str.format() function
# *********************************

# example 01:
text = 'Hello, {}'.format("Kasun")
print(text)

# example 02:
text = '{} your age is {}'.format("Kasun", 25)
print(text)

# example 03:
text = '{name} your age is {age}'.format(age=27, name="Falan")
print(text)

# *********************************
# Suing string Interpolation / f-Strings
# *********************************

name = "Chamari"

# example 04:
text = f'Hello, {name}'
print(text)

# example 05:
num1 = 50
num2 = 100

text = f'{num1} + {num2} = {num1 + num2}.'
print(text)

# example 06: 
def sayHello(firstName, lastName):
    return f'Hello, {firstName} {lastName}!' # this is a time saving

text = sayHello("Falan", "Andrea")
print(text)

# example 07: 
def sayHello(firstName, lastName):
    return f'Hello,' + ' ' + firstName + ' ' + lastName + '!' # this is a time wasting

text = sayHello("Falan", "Andrea")
print(text)

