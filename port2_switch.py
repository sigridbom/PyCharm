# Portfolio exam part 2 - Transfer an algorithm into Python code
# import needed libraries
import random

# create a function which sorts numbers in ascending or descending order,
# depending on the variable z (z = 1 or -1)
def sort_numbers(numlist, z): # the function take a list of numbers and a variable z as input

    print('Here is the non-sorted list:')
    print(numlist, '\n')  # print the non-sorted list and add a new line

    # the variable switch must be defined as 1 to start the algorithm
    switch = 1

    numlist_z = [] #create an empty list
    # loop through the list of numbers multiplying each number with z
    for number in numlist:
        result = number * z
        numlist_z.append(result) # append the result to the empty list

    # create a while loop which continues the loop as long as 'switch' is not equal to 0
    while switch != 0:
        x = 0  # is used to index the first number in the pair
        y = 1  # is used to index the second number in the pair
        switch = 0  # switch is set to 0 before the list is looped through

        # loop through the list
        # if the first number is bigger than the second number, switch the positions of the two
        for number in numlist_z:
            if numlist_z[x] > numlist_z[y]:
                numlist_z[y], numlist_z[x] = numlist_z[x], numlist_z[y] #swap the numbers
                # count each time two numbers have been switched looping through the entire list
                switch += + 1

            # if x is not at the second to last position of the list, increase the value of x with 1
            if x != len(numlist_z) - 2:
                x += 1

            # if y is not at the last position of the list, increase the value of y with 1
            if y != len(numlist_z) - 1:
                y += 1

        # create an empty list
        sorted_list = []
        # loop through the list multiplying each number with z again
        for number in numlist_z:
            result = number * z
            sorted_list.append(result)

    print('Here is the sorted list:')
    return(sorted_list)  # the function returns the sorted list

# creating a list of random numbers using random.randient from the random library
list = []  # creates an empty list
for i in range(1, 31):  # loop through 30 elements
    n = random.randint(1, 100)  # with numbers between 1 and 100
    list.append(n)  # append the numbers to the list

# call the function and use the generated list of random numbers as input
# if z = 1 the list will be in ascending order
# if z = -1 the list will be in descending order
print(sort_numbers(list, -1))