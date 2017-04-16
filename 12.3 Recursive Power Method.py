# Design a function that uses recursion to raise a number to a power. The function should accept two arguments: the number to be raised and the exponent. Assume that the exponent is a positive integer.


def main():
    # Get the product of the base raised to the exponent
    x = get_power(3, 4)

    # Displays the product
    print(x)


# The get_power function accepts two arguments, base and exp
# and returns the product of base raised to exp
def get_power(base, exp):
    if exp == 0:
        return 1
    else:
        exp -= 1
        return base * get_power(base, exp)

# Call the main function
main()
