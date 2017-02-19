# Many financial experts advise that property owners should insure
# their homes or buildings for at least 80 percent of the amount it would cost to replace the structure.
# Write a program that asks the user to enter the replacement cost of a building,
# and then displays the minimum amount of insurance he or she should buy for the property.

# Use a function to get the amount to replace the building from the customer.
# Use a second function to calculate the cost. Pass a parameter from the function
# that gets the cost to the function that calculates the amount to insure the building for.
# Display the amount with appropriate descriptive text in the second function.
# Assign meaningful names to your functions and variables.
# Every function also needs a comment explaining what it does and what other function it works with.


def cost():
    # This function asks the user to enter the amount it will cost to replace a building,
    # creates a variable of the users input,
    # passes the variable to the function replace,
    # and calls the function insurance.
    cost_of_replacement = float(input('Enter the replacement cost of the building: '))
    insurance(cost_of_replacement)


def insurance(cost_of_replacement):
    # This function accepts the variable cost_of_replacement from the function cost,
    # sets it to 0.8,
    # and prints a statement.
    insurance_value = cost_of_replacement * 0.8
    print("The minimum amount of insurance recommended is need is $", format(insurance_value, ",.2f"), sep="")
cost()
