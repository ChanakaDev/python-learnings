'''
************************************
break & continue keywords
************************************
'''

# example (01) print 1 - 10 numbers, but breake when meets 7
# ==========================
for number in range (1,11):
    if number == 7:
        break
    print(number)

# print 11 - 20 numbers, but skip if it meets 15
# ==========================
for number in range (11,21):
    if number == 15:
        continue
    print(number)