# Portfolio exam part 2 - Design an algorithm

# import libraries needed
import random

# create a function which sorts numbers in ascending order
def sort_numbers(numlist): # the function take a list of numbers as input

    print('Here is the non-sorted list:')
    print(numlist)

    # the variable switch must be defined as 1 to start the algorithm
    switch = 1

    # create a while loop which continues the loop as long as 'switch' is not equal to 0
    while switch != 0:
        x = 0  # is used to index the first number in the pair
        y = 1  # is used to index the second number in the pair
        switch = 0  # switch is set to 0 before the list is looped through

        # create a loop: for every number in the list, if the first number is bigger than the second number, switch the positions of the two
        for number in numlist:
            if numlist[x] > numlist[y]:
                numlist[y], numlist[x] = numlist[x], numlist[y] #swap the numbers
                # count each time two numbers have been switched looping through the entire list
                switch = switch + 1

            # if x is not at the second to last position of the list, increase the value of x with 1
            if x != len(numlist) - 2:
                x += 1

            # if y is not at the last position of the list, increase the value of y with 1
            if y != len(numlist) - 1:
                y += 1

    print('Here is the sorted list:')
    return(numlist)  # the function returns the sorted list

# creating a list of random numbers using random.randient from the random library

list = [] # creates an empty list
for i in range(1,31):  # makes a list of 30 numbers
    n = random.randint(1,100)  # with numbers between 1 and 100
    list.append(n)  # append the numbers to the list

# call the function and use the generated list of random numbers as input
print(sort_numbers(list))