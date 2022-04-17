'''
*************************
Important
*************************
    (*) we cannot directly pass other functions inside python print function
    (*) because if we do like that, it prints 'None'


'''
# # Example: 
# # ==============================
# letters = ["C", "a", "B", "A", "c", "b"]
# letters.sort()
# print(letters) # Output: ['A', 'B', 'C', 'a', 'b', 'c']

# print(letters.sort()) # Output: None


'''
*************************
Important
*************************
    (*) but that is okay for nomal functions with return statement
    (*) it means you can call user defined functions inside print()
'''

# # Example: 
# # ==============================
# def sayHello(fname):
#     return f'Hello {fname}!'

# print(sayHello("Falan")) # Output: Hello Falan!

