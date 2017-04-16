# Design a function that accepts a list of numbers as an argument. The function should recursively calculate the sum of all the numbers in the list and return that value.


def main():
    # Create a list of number
    l_st = [1, 3, 4, 2, 5]

    # Get the sum of the items in l_st
    x = get_sum(l_st)

    # Display the sum
    print(x)


# The get_sum function returns the sum of lst
def get_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + get_sum(lst[1:])

# Call the main function
main()
