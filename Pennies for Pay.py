# Write a program that calculates the amount of money a
# person would earn over a period of time if his or her
# salary is one penny the first day, two pennies the
# second day, and continues to double each day.
# The program should ask the user for the number of days.
# Display a table showing what the salary was for each day,
# and then show the total pay at the end of the period.
# The output should be displayed in a dollar amount, not the number of pennies

number_of_days_worked = int(input("Enter the number of days you have worked:"))
total_pennies = 0

print()

print("Day\t    Salary\n----\t------")
for current_day in range(number_of_days_worked):
    pennies_for_the_day = 2 ** current_day
    total_pennies += pennies_for_the_day
    print(current_day + 1, "\t\t", pennies_for_the_day)
total_pay = total_pennies * 0.01
print( "\nTotal pay: $", total_pay, sep="")
