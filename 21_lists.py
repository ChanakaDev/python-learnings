'''
*****************************
Lists basics
*****************************
'''

fruitList = ["Banana", "Apple", "Mango"]

# ordered: values can be accessed through indexes
# ----------------------------------
print(fruitList[0]) # Output: Banana
print(fruitList[1]) # Output: Apple
print(fruitList[2]) # Output: Mango

# mutable: values can be changed
# ----------------------------------
print(fruitList) # Output: ['Banana', 'Apple', 'Mango']
fruitList[0] = "Mangus"
print(fruitList) # Output: ['Mangus', 'Apple', 'Mango']

# allow duplicates
# ----------------------------------
fruitList = ["Banana", "Apple", "Mango", "Mango", "Mango"]
print(fruitList) # Output: ['Banana', 'Apple', 'Mango', 'Mango', 'Mango']

# length of the list
# ----------------------------------
print(len(fruitList)) # Output: 5

# different types of data can be hold
# ----------------------------------
list1 = [1,2,3,4,5]
list2 = ["item1", "item2", "item3", "item4"]
list3 = [True, True, False, False]

studentData = ["Kasun", 25, "Male", True]

# make a list/ list constructor
# ----------------------------------
namesList = list(("name1", "name2", "name3", "name4")) # (()) two brackets 
print(namesList) # Output: ['name1', 'name2', 'name3', 'name4']

'''
*****************************
Access list items
*****************************
'''

exampleList = ["0index", "1index", "2index", "3index", "4index"]
print(exampleList[0]) # Output: 0index
print(exampleList[-1]) # Output: 4index (index -1 means last item)
print(exampleList[2:5]) # Output: ['2index', '3index', '4index'] (output comes as a list)
print(exampleList[:4]) # Output: ['0index', '1index', '2index', '3index'] (from start to 4-1 index)
print(exampleList[:10]) # Output: ['0index', '1index', '2index', '3index', '4index'] no errors - lol :)
print(exampleList[2:]) # Output: ['2index', '3index', '4index']
print(exampleList[-4:-1]) # Output: ['1index', '2index', '3index']
print(exampleList[:-1]) # Output: ['0index', '1index', '2index', '3index'] 
# (no start mentioned, so from start to -1 index, to the last index)


'''
*****************************
Check an item is exist
*****************************
'''

fruitList = ["Banana", "Apple", "Mango", "Papaya"]
favoriteFruit = "Banana"

if favoriteFruit in fruitList:
    print("Your favorite fruit is there")
else: 
    print("It is not there")


'''
*****************************
Change list items
*****************************
'''

# Example 01: Change one item
girlsNames = ["Falan", "Ashanya", "Randilu", "Muthumini"]
girlsNames[0] = "Falan Adria"
print(girlsNames) # Output: ['Falan Adria', 'Ashanya', 'Randilu', 'Muthumini']

# Example 02: Change range of items
boysNames = ["Kasun", "Harsha", "Kakulu", "Senaka"]
boysNames[0:2] = ["Denuwan", "Ashen", "Siril"]
print(boysNames) # Output: ['Denuwan', 'Ashen', 'Siril', 'Kakulu', 'Senaka']

boysNames = ["Kasun", "Harsha", "Kakulu", "Senaka"]
boysNames[0:3] = ["Denuwan", "Ashen", "Siril"]
print(boysNames) # Output: ['Denuwan', 'Ashen', 'Siril', 'Senaka']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # Output: ['apple', 'watermelon'] 2 values has replaced with a one value

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # Output: ['apple', 'banana', 'watermelon', 'cherry']
# new value has replaced the index 2 and, the existing value of it has moved forward

'''
*****************************
Add new list items
*****************************
'''
'''
Not like arrays, here we have
-----------------------------
    (*) append  - to add items
    (*) pop     - to remove items
'''

# Example 01: Using list.append()
# =======================================
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # Output: ['apple', 'banana', 'cherry', 'orange'] has appened to the end

# Example 02: Using list.insert(index, value)
# =======================================
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # Output: ['apple', 'orange', 'banana', 'cherry'] insert to the mentioned index, move others forward

# Example 03: Extend a list (using arr.extend(arr,newArr))
# =======================================
thislist = ["apple", "banana", "cherry"]
fruits = ["mango", "pineapple", "papaya"]
thislist.extend(fruits)
print(thislist) # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Example 04: Extend a list (using + operator)
# =======================================
thislist = ["apple", "banana", "cherry"]
fruits = ["mango", "pineapple", "papaya"]
thislist = thislist + fruits
print(thislist) # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Example 05: Extend() with other collections (set, tuple, dict)
# =======================================
student1 = ["Asela", 22, "Male"]
student2 = {
    "name" : "Kamala",
    "age" : 21,
    "gender" : "Female"
}
print(student1 + student2) # Output: TypeError: can only concatenate list (not "dict") to list

student1.extend(student2)
print(student1) # Output: ['Asela', 22, 'Male', 'name', 'age', 'gender']

student1 = ["Asela", 22, "Male"]
student2 = ("Kamala" , 21, "Female")
# print(student1 + student2) # Output: TypeError: can only concatenate list (not "tuple") to list
student1.extend(student2)
print(student1) # Output: ['Asela', 22, 'Male', 'Kamala', 21, 'Female']


'''
*****************************
Remove list items
*****************************
'''
# 01: Remove Specified Item
# =====================================
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # Output: ['apple', 'cherry']

# 02: Remove Specified Index
# =====================================
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # Output: ['apple', 'cherry']

# 03: Remove last index
# =====================================
thislist = ["apple", "banana", "cherry"]
thislist.pop() # no index means, last index
print(thislist) # Output: ['apple', 'banana']

# 04: Remove Specified Index (using del)
# =====================================
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # Output: ['banana', 'cherry']

# 05: Delete entire list
# =====================================
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) # Output: NameError: name 'thislist' is not defined

# 06: Clean a list (no delete)
# =====================================
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # Output: []


'''
*****************************
Loop through lists
*****************************
'''

'''
Using for loop
=============================
'''
thislist = ["apple", "banana", "cherry"]
for fruit in thislist:
  print(fruit)
# Output:
# apple
# banana
# cherry

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i, thislist[i])
# Output:
# 0 apple
# 1 banana
# 2 cherry

'''
Using while loop
=============================
'''
# Use list.len() to determine length of the list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

'''
Using while comprehension
=============================
'''
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


'''
*****************************
Sort list items
*****************************
'''

# 01: Sort Alphanumerically
# ===========================
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# 02: Sort Numerically
# ===========================
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # Output: [23, 50, 65, 82, 100]

# 03: Sort Descending
# ===========================
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # Output: [100, 82, 65, 50, 23]

'''
sort() is a case sensituve method
----------------------------------
    (*) resulting in all capital letters being sorted before lower case letters:
'''

letters = ["C", "a", "B", "A", "c", "b"]
letters.sort()
print(letters) # Output: ['A', 'B', 'C', 'a', 'b', 'c']

'''
case insensitive sort
---------------------------------
    (*) suppose you have to sort list of words. But starting letter of the some words are capitalized 
    (*) in this type of situation, what you have to do is to specify a sort key 
    (*) sort key must be lowercase/ uppercase
'''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # Output: ['banana', 'cherry', 'Kiwi', 'Orange']

'''
reverse()
---------------------------------
    (*) reverses the current sorting order of the elements.
'''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


'''
*****************************
Copy lists
*****************************
'''

'''
Why we need copy() function?
-----------------------------
    (*) You cannot copy a list simply by typing list2 = list1, 
        because: list2 will only be a reference to list1, 
        and changes made in list1 will automatically also be made in list2.
    (*) To differentiate, the copied list from original list 
        we need the copy function
'''

# Example 01: without copy
# =========================
thislist = ["apple", "banana", "cherry"]
mylist = thislist
thislist[0] = "mangus"
print(thislist) # Output: ['mangus', 'banana', 'cherry']
print(mylist)   # Output: ['mangus', 'banana', 'cherry']

# Example 02: with copy
# =========================
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
thislist[0] = "mangus"
print(thislist) # Output: ['mangus', 'banana', 'cherry']
print(mylist)   # Output: ['apple', 'banana', 'cherry']

'''
*****************************
Combine 2 lists
*****************************
'''

# 1st method: using + operator
# ============================
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) # Output: ['a', 'b', 'c', 1, 2, 3]


# 2nd method: using listName.append() function
# append happens: letter by letter
# ============================
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) # Output: ['a', 'b', 'c', 1, 2, 3]


# 3rd method: using listName.extend() function
# ============================
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) # Output: ['a', 'b', 'c', 1, 2, 3]

'''
Short Note
==============================
* append()	    - Adds an element at the end of the list
* clear()	    - Removes all the elements from the list
* copy()	    - Returns a copy of the list
* count()	    - Returns the number of elements with the specified value
* extend()	    - Add the elements of a list (or any iterable), to the end of the current list
* index()	    - Returns the index of the first element with the specified value
* insert()	    - Adds an element at the specified position
* pop()	        - Removes the element at the specified position
* remove()	    - Removes the item with the specified value
* reverse()	    - Reverses the order of the list
* sort()	    - Sorts the list
'''