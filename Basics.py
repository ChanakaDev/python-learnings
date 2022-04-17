'''
Python Lists
=====================================================
    (*) stores similar or different data types
    (*) new items added to the end of the list

    (*) indexing: data can be accessed by "indexes"
    (*) duplicates: duplicates are allowed
    (*) mutable: items can be changed
'''

# listOfData = ['car', 'van', 'boat', 'bike', 12]
# print(listOfData)
# operations with lists

'''
Python Tuples
=====================================================
    (*) ordered
    (*) indexing: data can be accessed by "indexes"
    (*) duplicates: duplicates are allowed
    (*) immutable: items cannot be changed
'''

# tupleOfData = ('car', 'van', 'boat', 'bike', 12)
# print(tupleOfData)
# operations with tuples

'''
Python Sets
=====================================================
    (*) unordered
    (*) no indexing: data cannot be accessed by indexes
    (*) no duplicates: duplicates are not allowed
    (*) immutable: items cannot be changed
'''

# setOfData = {'car', 'van', 12, True}
# print(setOfData)
# operations with sets

'''
Python dictonary
=====================================================
    (*) unordered 
    (*) no duplicates: duplicates are not allowed
    (*) mutable: items can be changed

    (*) key: value pairs
    (*) items can be accessed using keys
'''

# dictOfData = {  'name': 'Ann', 
#                 'age': 20, 
#                 'citiesLived': ['Colombo', 'Kandy'] }
# print(dictOfData)
# operations with dictonaries 

'''
Python functions
=====================================================
'''
# # readability
# def printAdress():
#     name = "Kamal Jayasundara"
#     houseNo = "No. 443"
#     street = "Gampola"
#     city = "Kandy"
#     adreess = name + '\n' + houseNo + '\n' + street + '\n' + city
#     print(adreess)

# print("out of the scope of the printAdress()")

# # reusability
# printAdress()
# printAdress()
# printAdress()
# printAdress()

'''
function arguments & parameters
=====================================================
'''
# # Q. Write a function to make full name from fisrtname and lastname

# def makeFullName(firstName, lastName): # parameters
#     fullName = firstName + " " + lastName
#     print("Full Name = " + fullName)

# makeFullName("nameA", "nameAA") # arguments
# makeFullName("nameB", "nameBB")
# makeFullName("nameC", "nameCC")
# makeFullName("nameD", "nameDD")

'''
Arbitrary Arguments/ Variable Length Arguments
    (*) when there are unknown number of arguments
=====================================================
'''

# def sayAyubowan(*names): # take all the arguments in to a tuple
#     for name in names:
#         print("Ayuowan " + name + "!")
    
# sayAyubowan("A", "B", "C", "D", "E")

'''
Keyword Arguments
    (*) specify arguments in a different order
=====================================================
'''

# def printYourAge(name, age):
#     print(name +' your age is, '+ str(age))

# printYourAge("A", 24)
# printYourAge(age=24, name="B")

'''
Python **kwargs
Arbitrary Keyword Arguments
=====================================================
'''
# # example dictonary
# student = {'name' : 'A', 'age' : 24}
# print(student['name'])

# def printName(** studentDetails):
#   print("Your first name is " + studentDetails["firstName"])

# printName(firstName="Kamal", lastName="Jayasundara", age=12, mathsMarks=98)

'''
Lists, Tuples, Sets or Dictionary can be passed
as Arguments
=====================================================
'''

# students = ["A", "B", "C", "D", "E", "F"]

# def printFirstStudentName(students):
#     print('first student is: ' + students[0])
#     print('last student is: ' + students[-1])

# printFirstStudentName(students)

'''
Default values, in function arguments
=====================================================
'''

# def addNumbers(num1 = 0): # default value
#     sum = num1 + 10
#     print("sum = " + str(sum))

# addNumbers()
# addNumbers(200)

'''
return statement
    (*) function execution ends from the return statement
    (*) function may or may not have a return
=====================================================
'''

# def calcSum():
#     num1 = 10
#     num2 = 50
#     sum = num1 + num2
#     return sum
#     print('hi') # useless (not working after retun statement)

# output = calcSum()
# print(output)

'''
recursive function
    (*)  A function, which can be called within itself 
=====================================================
'''

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return (num * factorial(num-1))
#         # 3 * factorial(3-1)
#         # 2 * factorial(2-1)
#         # 1

#         # 3 * 2 * 1 = 6

# print(factorial(3))

'''
lambda functions (Anonymous function)
=====================================================
    A function without a name 
    Many arguments, one expression 
    Useful when a function is needed for a short time
'''

# sumOfTwoNumbers =  lambda x, y: (x+y)
# print(sumOfTwoNumbers(2,2)) # output: 4

# lambdaFunction =  lambda num1, num2, num3: (num1+num2+num3)
# print(lambdaFunction(2,2,2))

'''
Good example lambda function
=====================================================
'''
# def myfunc(n):
#   return lambda a : a * n # lambda a : a * 3

# mytripler = myfunc(3) # lambda a : a * 3
# # mytripler = lambda a : a * 3

# print(mytripler(11)) # mytripler = lambda 11 : 11 * 3
# # output: 11 * 3 = 33