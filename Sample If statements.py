# Write a program that asks the user for a number in the range of 1 through 7.
# The program should display the corresponding day of the week,
# where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.
# he program should display an error message if the user enters a number that is outside the range of 1 through 7.

x = input("Enter a number in the range of 1 through 7: ")
if x == str("1"):
    print("Monday")
elif x == str("2"):
    print("Tuesday")
elif x == str("3"):
    print("Wednesday")
elif x == str("4"):
    print("Thursday")
elif x == str("5"):
    print("Friday")
elif x == str("6"):
    print("Saturday")
elif x == str("7"):
    print("Sunday")
else:
    print("ERROR")
