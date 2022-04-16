'''
********************************
iterative statements
********************************
    (*) 1st type loops: iterate until a condition is unsatisfactory
    (*) 2nd type loops: iterate over a sequence

    (*) looging statements
        (*) for loops   : for already known number of times
        (*) while loops : for already unknown number of times
'''

# example: print numbers from 1 to 10
# ===================================
# (1) using a for loop
number = 1
while number <= 10:
    print("number is: " + str(number))
    number+=1

# (2) using a while loop
for number in range (1, 11):
    print("number is: " + str(number))

'''
Python for loop examples
==========================
'''

'''
(*) for <item> in <list>
(*) for <letter> in <word>
(*) for number in range (end+1):
(*) for number in range(start, end+1):
(*) for number in range(start, end+1, step):    
'''

# (01) Print each fruit in a fruit list
# ===================================
fruits = ["mango","banana","apple"]
for fruit in fruits:
    print(fruit)

# (02) Print each letter of the following word
# ===================================
word = "example"
for letter in word:
    print(letter)

# (03) Print the integers from 0 upto 5 
# ===================================
for number in range (6):
    print(number) # 0 1 2 3 4 5

# (04) Print the numbers from 1-100
# ===================================
for number in range (1,101):
    print(number) # 1-100 with a and 100

# (05) Print even numbers from 0 - 100
# ===================================
for number in range (0,101,2):
    print(number)