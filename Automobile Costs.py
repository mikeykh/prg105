# Write a program that asks the user to enter the
# monthly costs for the following expenses incurred from operating
# his or her automobile: loan payment, insurance, gas, oil, tires and maintenance.
# The program should then display the total monthly cost of these expenses,
# and the total annual cost of these expenses.
# Assign meaningful names to your functions and variables.
# Every function also needs a comment explaining
# what it does and what other function it works with.

# Function 1:
# Gather information from user
# Accumulate the total in a local variable
# Print the monthly costs on screen, formatted appropriately for money
# Pass the monthly cost to Function 2

# Function 2:
# Accepts a float parameter
# Calculates yearly cost by multiplying monthly cost by 12
# Displays the yearly cost on screen, formatted appropriately for money


def calculate_total_monthly_cost():
    # This function is used to gather all of the information,
    # adds all of the users inputs and sets the sum to a variable,
    # passes the variable to the function calculate_total_yearly_cost,
    # and calls the function calculate_total_monthly_cost.
    loan = float(input("Please enter your car payment: "))
    insurance = float(input("Please enter your the amount of your insurance payment: "))
    gas = float(input("Please enter your monthly gas expense: "))
    oil = float(input("Please enter your monthly oil expense: "))
    tire = float(input("Please enter your monthly expense for tires: "))
    maintenance = float(input("Please enter your monthly maintenance expense: "))
    total_monthly_cost = loan+insurance+gas+oil+tire+maintenance
    print("This is the total monthly cost: $", format(total_monthly_cost, ",.2f"), sep="")
    calculate_total_yearly_cost(total_monthly_cost)


def calculate_total_yearly_cost(total_monthly_cost):
    # This function calculates and prints the total yearly cost
    # and is called by the function calculate_total_monthly_cost.
    yearly_total = total_monthly_cost * 12
    print("This is the yearly cost: $", format(yearly_total, ',.2f'), sep="")

calculate_total_monthly_cost()
