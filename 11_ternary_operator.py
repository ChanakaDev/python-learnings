'''
Ternary operator in Python
    (*) one-line if else statement
    (*) It's LOL :)
=====================================================
Syntax: [on_true] if [expression] else [on_false] 
'''

# example 01:
print("Correct") if 5<10 else print("Wrong")

# example 02:
salaryInDollars = 3500
print("You can love") if salaryInDollars>1000 else print("you cannot love")

# example 03:
# # technique
# x = 70
# print("A") if x >= 75 
# else print("B") if x >= 65 
# else print("C") if x >= 55 
# else print("S") if x >= 35 
# else print("F")

x = 70 
print("A") if x >= 75 else print("B") if x >= 65 else print("C") if x >= 55 else print("S") if x >= 35 else print("F")