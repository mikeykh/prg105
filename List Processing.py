# Have a function that creates a list with
# 20 random integers between 1 and 100
# (Assign them dynamically, store the list in a variable.)

# Have a function get a number from the user
# that is between 1 and 100
# (validate for errors using a try and except statement).

# Pass both the list and the user's number
# to a function and have it display all numbers
# in the list that are greater than the users number.
# If there are not any, display a message that
# explains there are no numbers in the
# list greater than the entered number.

# Appropriately name variables and functions,
# include at least one comment for each function,
# upload to GitHub and hand in a link to the program.


import random
# Import the module called random


def rand_lst():
    # Put 20 random numbers into a list.
    rand_num_lst = []
    for i in range(20):
        rand_num_lst.append(random.randint(1, 100))
    return rand_num_lst


def user_input():
    # ask the user to input a number.
    # except a value error and explain to the user how to fix it.
    user_num = int(input("Enter a number from 1 to 100: "))
    try:
        if 1 <= user_num <= 100:
                    return user_num
    except ValueError:
        print("You must enter a number between 1 and 100")
    

def new_lst(rand_num_lst, user_num):
    # Check if any numbers are in the list are greater than the users number.
    try:
        lst = [i for i in rand_num_lst if i > user_num]
        if len(lst) == 0:
            return print("There are no numbers in the list that are greater than", user_num)
        else:
            return print("The number(s) greater than", user_num, "in a random list of 20 numbers are:", lst)
    except TypeError:
        print("You must enter a number from 1 to 100.")


def main():
    # Call the previous functions into a concise function.
    user_num = user_input()
    rand_num_lst = rand_lst()
    new_lst(rand_num_lst, user_num)


main()
# Call the main function.
