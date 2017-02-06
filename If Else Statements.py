# Write a program that prompts the user to enter a number within the range of 1 through 10.
# The program should display the roman numeral version of that number.
# If the number is outside the range of 1 through 10, the program should display an error message.

x = input("Enter a number in the range of 1 through 10: ")
if x == str("1"):
    print("I")
elif x == str("2"):
    print("II")
elif x == str("3"):
    print("III")
elif x == str("4"):
    print("IV")
elif x == str("5"):
    print("V")
elif x == str("6"):
    print("VI")
elif x == str("7"):
    print("VII")
elif x == str("8"):
    print("VIII")
elif x == str("9"):
    print("IX")
elif x == str("10"):
    print("X")
else:
    print("ERROR")
