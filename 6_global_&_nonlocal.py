'''
********************************************
example: someone hide inside a cardboard box
********************************************
'''
x = "global x"
def outer():
    x = "outer x"
    def inner():
        x = "inner x"
        print(x) # print: inner x 
    inner()
    print(x) # print: outer x
outer() 
print(x) # print: global x

'''
output:
    inner x
    outer x
    global x
'''

'''
=========================================
global Vs. nonlocal
=========================================
global      : make local variables, can be accessed in the global scope  
nonlocal    : make outerFun() can change innerFun() variables

'''

x = "global x" 
def inner():
    global x 
    # then we can change value of the x
    # inside a fun()
    x = "inner x" 
inner() 
print(x)

# nonlocal example 01
def outer():
    x=5
    def inner():
        nonlocal x
        x=x+3 # this x is a new x, if we did'nt make this nonlocal
        print(x)
    inner() # 1st we run this
outer() # 2nd we run this

# nonlocal example 02
def existingName():
  name = "value 1" # local
  def changeName():
    nonlocal name 
    name = "value 2" # enclosing
  changeName() 
  return name

print(existingName())