'''
*****************************
Lists basics
*****************************
'''

# fruitList = ["Banana", "Apple", "Mango"]

# # ordered: values can be accessed through indexes
# # ----------------------------------
# print(fruitList[0]) # Output: Banana
# print(fruitList[1]) # Output: Apple
# print(fruitList[2]) # Output: Mango

# # mutable: values can be changed
# # ----------------------------------
# print(fruitList) # Output: ['Banana', 'Apple', 'Mango']
# fruitList[0] = "Mangus"
# print(fruitList) # Output: ['Mangus', 'Apple', 'Mango']

# # allow duplicates
# # ----------------------------------
# fruitList = ["Banana", "Apple", "Mango", "Mango", "Mango"]
# print(fruitList) # Output: ['Banana', 'Apple', 'Mango', 'Mango', 'Mango']

# # length of the list
# # ----------------------------------
# print(len(fruitList)) # Output: 5

# # different types of data can be hold
# # ----------------------------------
# list1 = [1,2,3,4,5]
# list2 = ["item1", "item2", "item3", "item4"]
# list3 = [True, True, False, False]

# studentData = ["Kasun", 25, "Male", True]

# # make a list/ list constructor
# # ----------------------------------
# namesList = list(("name1", "name2", "name3", "name4")) # (()) two brackets 
# print(namesList) # Output: ['name1', 'name2', 'name3', 'name4']

'''
*****************************
Access list items
*****************************
'''

# exampleList = ["0index", "1index", "2index", "3index", "4index"]
# print(exampleList[0]) # Output: 0index
# print(exampleList[-1]) # Output: 4index (index -1 means last item)
# print(exampleList[2:5]) # Output: ['2index', '3index', '4index'] (output comes as a list)
# print(exampleList[:4]) # Output: ['0index', '1index', '2index', '3index'] (from start to 4-1 index)
# print(exampleList[:10]) # Output: ['0index', '1index', '2index', '3index', '4index'] no errors - lol :)
# print(exampleList[2:]) # Output: ['2index', '3index', '4index']
# print(exampleList[-4:-1]) # Output: ['1index', '2index', '3index']
# print(exampleList[:-1]) # Output: ['0index', '1index', '2index', '3index'] 
# # (no start mentioned, so from start to -1 index, to the last index)


'''
*****************************
Check an item is exist
*****************************
'''

# fruitList = ["Banana", "Apple", "Mango", "Papaya"]
# favoriteFruit = "Banana"

# if favoriteFruit in fruitList:
#     print("Your favorite fruit is there")
# else: 
#     print("It is not there")


'''
*****************************
Change list items
*****************************
'''

# # Example 01: Change one item
# girlsNames = ["Falan", "Ashanya", "Randilu", "Muthumini"]
# girlsNames[0] = "Falan Adria"
# print(girlsNames) # Output: ['Falan Adria', 'Ashanya', 'Randilu', 'Muthumini']

# # Example 02: Change range of items
# boysNames = ["Kasun", "Harsha", "Kakulu", "Senaka"]
# boysNames[0:2] = ["Denuwan", "Ashen", "Siril"]
# print(boysNames) # Output: ['Denuwan', 'Ashen', 'Siril', 'Kakulu', 'Senaka']

# boysNames = ["Kasun", "Harsha", "Kakulu", "Senaka"]
# boysNames[0:3] = ["Denuwan", "Ashen", "Siril"]
# print(boysNames) # Output: ['Denuwan', 'Ashen', 'Siril', 'Senaka']

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist) # Output: ['apple', 'watermelon'] 2 values has replaced with a one value

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist) # Output: ['apple', 'banana', 'watermelon', 'cherry']
# # new value has replaced the index 2 and, the existing value of it has moved forward

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

# # Example 01: Using list.append()
# # =======================================
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist) # Output: ['apple', 'banana', 'cherry', 'orange'] has appened to the end

# # Example 02: Using list.insert(index, value)
# # =======================================
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist) # Output: ['apple', 'orange', 'banana', 'cherry'] insert to the mentioned index, move others forward

# # Example 03: Extend a list (using arr.extend(arr,newArr))
# # =======================================
# thislist = ["apple", "banana", "cherry"]
# fruits = ["mango", "pineapple", "papaya"]
# thislist.extend(fruits)
# print(thislist) # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# # Example 04: Extend a list (using + operator)
# # =======================================
# thislist = ["apple", "banana", "cherry"]
# fruits = ["mango", "pineapple", "papaya"]
# thislist = thislist + fruits
# print(thislist) # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# # Example 05: Extend() with other collections (set, tuple, dict)
# # =======================================
# student1 = ["Asela", 22, "Male"]
# student2 = {
#     "name" : "Kamala",
#     "age" : 21,
#     "gender" : "Female"
# }
# print(student1 + student2) # Output: TypeError: can only concatenate list (not "dict") to list
# print(student1.extend(student2)) # Output: None
# print(student1.extend(student2)) # Output: None
# student1 = student1.extend(student2)
# print(student1) # Output: None

# student1 = ["Asela", 22, "Male"]
# student2 = ("Kamala" , 21, "Female")
# print(student1 + student2) # Output: TypeError: can only concatenate list (not "tuple") to list
# print(student1.extend(student2)) # Output: None


'''
*****************************
Remove list items
*****************************
'''
# # 01: Remove Specified Item
# # =====================================
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist) # Output: ['apple', 'cherry']

# # 02: Remove Specified Index
# # =====================================
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist) # Output: ['apple', 'cherry']

# # 03: Remove last index
# # =====================================
# thislist = ["apple", "banana", "cherry"]
# thislist.pop() # no index means, last index
# print(thislist) # Output: ['apple', 'banana']

# # 04: Remove Specified Index (using del)
# # =====================================
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist) # Output: ['banana', 'cherry']

# # 05: Delete entire list
# # =====================================
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist) # Output: NameError: name 'thislist' is not defined

# # 06: Clean a list (no delete)
# # =====================================
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist) # Output: []


'''
*****************************
Loop through lists
*****************************
'''

'''
Using for loop
=============================
'''
# thislist = ["apple", "banana", "cherry"]
# for fruit in thislist:
#   print(fruit)
# # Output:
# # apple
# # banana
# # cherry

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(i, thislist[i])
# # Output:
# # 0 apple
# # 1 banana
# # 2 cherry

'''
Using while loop
=============================
'''
# # Use list.len() to determine length of the list
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

'''
Using while comprehension
=============================
'''
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


'''
*****************************
Sort list items
*****************************
'''

# # 01: Sort Alphanumerically
# # ===========================
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist) # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# # 02: Sort Numerically
# # ===========================
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist) # Output: [23, 50, 65, 82, 100]

# # 03: Sort Descending
# # ===========================
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist) # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist) # Output: [100, 82, 65, 50, 23]

'''
sort() is a case sensituve method
----------------------------------
    (*) resulting in all capital letters being sorted before lower case letters:
'''

# letters = ["C", "a", "B", "A", "c", "b"]
# letters.sort()
# print(letters) # Output: ['A', 'B', 'C', 'a', 'b', 'c']

# print(letters.sort()) # Output: None

'''
<todo>: check all above again for 'None' outputs
'''

