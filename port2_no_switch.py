# Portfolio part 2
# Sorting a list of numbers numerically

import random

#create a random list of 20 numbers
numlist = []
for i in range(1,31):
    n = random.randint(1,100)
    numlist.append(n)
print('Here is the non-sorted list')
print(numlist)

# making an algorithmic loop to sort the list numerically
# defining starting variables
counter = 0

while counter != len(numlist):
    x = 0
    y = 1
    no_switch = 0
    for number in numlist:
        if numlist[x] > numlist[y]:
            numlist[y], numlist[x] = numlist[x], numlist[y] #swap the numbers
        else:
            no_switch = no_switch + 1

        if x != len(numlist) -2:
            x += 1
        if y != len(numlist) -1:
            y += 1
    counter = no_switch
print('Here is the sorted list')
print(numlist)
print('Done')



