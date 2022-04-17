'''
*******************************
Strings
*******************************
(*) immutable
(*) indexing and negative indexing supports
(*) no separate char data type in python
'''
# Example (01): length of a string
text = "Falan Andria"
print(len(text)) # Output:  12

# Example (02): check sub string is present
string = "You are the best"
subString = "You"
print(subString in string) # Output: True

# Example (03): check sub string is not present
string = "You are the best"
subString = "You"
print(subString not in string) # Output: False

# Example (04): delete a string
text = "this will be deleted"
print(text) # Output: this will be deleted
del(text)
print(text) # Output: NameError: name 'text' is not defined



'''
*******************************
String slicing
*******************************
(*) extract part of a string, as a sub string
'''

ourText = "I like to eat chocolate"

# positive indexing
print(ourText[0]) # Output: I
print(ourText[len(ourText)-1]) # Output: e (the last character)
print(ourText[25]) # IndexError: string index out of range

# negative indexing
print(ourText[-1]) # Output: e (the last character)
print(ourText[-len(ourText)]) # Output: I (the first character)
# =============================================================


emptyString = ""

print(len(emptyString)) # Output: 0
print(emptyString[0]) # Output: IndexError: string index out of range
print(emptyString[-1]) # Output: IndexError: string index out of range 
# =============================================================


spaceOnly = " "

print(len(spaceOnly)) # Output: 1
print(spaceOnly[0]) # Output: a empty space
print(spaceOnly[-1]) # Output: a empty space
# =============================================================



'''
**********************
[start : end+1 : step]
**********************
'''

newText = "Hello machan!"

print(newText[:]) # Output: Hello machan! (an exact copy) 
print(newText[::]) # Output: Hello machan! (an exact copy) same as above
print(newText[::1]) # Output: Hello machan! (an exact copy) same as above

print(newText[0:5]) # Output: Hello
print(newText[::2]) # Output: Hlomca! (ekak hera ekak)
print(newText[::-1]) # Output: !nahcam olleH (full reverse string)
print(newText[-1:0:-1]) # Output: !nahcam olle (reverse string without first character)

print(newText[-1:0]) # Output: empty space
print(newText[-1:0:1]) # Output: empty space



'''
**********************
String operators
**********************
'''
# example 01: + operator
# ----------------------
print("banana" + "apple") # Output: bananaapple

# example 02: * operator
# ----------------------
print("apple"*3) # Output: appleappleapple



'''
**********************
format() - same as the previpus note
**********************
'''

text = "Your birthday is {}/{}/{}"
formattedText = text.format("1995","04","14")
print(formattedText) # Output: Your birthday is 1995/04/14

text = "Your name is {0} {1}"
formattedText = text.format("Falan","Andria")
print(formattedText) # Output: Your name is Falan Andria

text = "{yourName} your friend is: {friendName}"
formattedText = text.format(yourName="Kasun",friendName="Falan")
print(formattedText) # Output: Kasun your friend is: Falan



'''
**********************
Other string functions
**********************
'''

testString = "Testing string"
# text.lower()
# ==========================
print(testString.lower()) # Output: testing string
# text.islower()
# ==========================
print(testString.islower()) # Output: False
# text.upper()
# ==========================
print(testString.upper()) # Output: TESTING STRING


# ==========================
# text.strip()/ lstrip()/ rstrip()
# ==========================
textWithSpaces = "     Text     "
print(textWithSpaces) # Output:     Text     (with spaces) 
print(textWithSpaces.strip()) # Output:Text(without spaces)
print(textWithSpaces.lstrip()) # Output:Text     (without leading/ left spaces)
print(textWithSpaces.rstrip()) # Output:     Text(without tailing/ right spaces)


# ==========================
# text1.replace(text1, text2)
# ==========================
text1 = "111111111111111"
text2 = "222222222222222"
print(text1.replace(text1, text2)) # Output: 222222222222222 (left side is replaced with right side)


# ==========================
# text.split(" ")
# ==========================
strForTesting = "This is a testing string"
result = strForTesting.split(" ")
print(result) # Output: ['This', 'is', 'a', 'testing', 'string'] (array of strings)

strForTesting = "this-is-a-commit-message"
result = strForTesting.split("-") # Output: ['this', 'is', 'a', 'commit', 'message']
print(result) 


# ==========================
# text.find("subString")
# ==========================
testString = "elephant house ice cream"
result = testString.find("ice")
print(result) # Output: 15 (index of the first occurance)
result = testString.find("apple")
print(result) # Output: -1 (this means not found)
result = testString.find("Ice")
print(result) # Output: -1 (not found, because case sensitive)


# ==========================
# text.isdigit()
# ==========================
from curses.ascii import isdigit

phoneNumber = "0777123456"
result = phoneNumber.isdigit()
print(result) # Output: True (no other characters)

idNumber = "889554681V"
result = idNumber.isdigit()
print(result) # Output: False (there is a letter)

