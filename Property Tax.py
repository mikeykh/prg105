# A county collects property taxes on the assessment value of property,
# which is 60 percent of the property's actual value.
# For example, if an acre of land is valued at $10,000, its assessment value is $6,000.
# The property tax is then 72 cents for each $100 of the assessment value.
# The tax for the acre assessed at $6,000 will be $43.20.

# Write a program that asks for the actual value of a piece of property
# and displays the assessment value and the property tax.

# Use meaningful names for your variables and function names.
# Add at least one comment per function describing what it does
# and what other functions it connects to.Create two separate functions.
# Function 1 should gather information from the user and pass that
# information to Function 2 which will perform the calculations and display a
# meaningful result with proper formatting for currency.


def property_value():
    # This function asks the user for the property's value,
    # creates a value called value and passes it to the function assessment,
    # calls the function assessment
    # and displays a meaningful result with the proper formatting for currency.
    value = float(input("Enter the property's actual value: "))
    assessment_value = value * 0.6
    print("The assessment value is $", format(assessment_value, ",.2f"), sep="")
    assessment(assessment_value)


def assessment(assessment_value):
    # This function calculate the property tax,
    # displays a meaningful result with the proper formatting for currency
    # and accepts the value assessment_value from the function property_value
    property_tax = assessment_value * 0.0072
    print("The property tax is $", format(property_tax, ",.2f"), sep="")
property_value()
