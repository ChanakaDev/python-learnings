'''
Flow Control
=====================================================
    (1) Decision making
        (*) single if
        (*) if else
        (*) elif keyword (else + if)
        (*) if elif else
        (*) ternary operator

    (2) Iterating 

'''
# single if condition
# ======================================
price = float(input("enter the price: "))
if price>50:
    print('high price')

# if else condition
# ======================================
age = int(input("enter your age: "))
if age >= 18:
    print('An adult')
else: 
    print('Not an adult')

# if else if
# nestead if else
# ======================================
marks = int(input("enter your marks: "))
if marks >= 0 and marks <= 100:
    if marks >= 75:
        print("Grade A")
    elif marks >= 65:
        print("Grade B")
    elif marks >= 55:
        print("Grade C")
    elif marks >= 35:
        print("Grade S")
    else:
        print("Failed")
else: 
    print("Invalid marks")