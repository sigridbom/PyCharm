import random

#create a random list of 20 numbers
numlist = []
for i in range(1,31):
    n = random.randint(1,100)
    numlist.append(n)
print('Here is the non-sorted list')
print(numlist)

#the same as port2 but counting the number of switches instead
counter = 1

while counter != 0:
    x = 0
    y = 1
    switch = 0
    for number in numlist:
        if numlist[x] > numlist[y]:
            numlist[y], numlist[x] = numlist[x], numlist[y] #swap the numbers
            switch = switch + 1

        if x != len(numlist) - 2:
            x += 1
        if y != len(numlist) - 1:
            y += 1

    counter = switch
print('Here is the sorted test list')
print(numlist)
print('Done')