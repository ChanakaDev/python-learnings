'''
************************************
nestead loops
************************************
'''

'''
(*) "in range" is used only with numbers
(*) "in" is used only with sequences(characters, list, tupe, dict..)
'''

'''
(*) So, don't use "in range" here range
(*) use only "in" 
'''

# Print each adjective for every fruit
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    for adjective in adjectives:
        print(adjective, fruit) 