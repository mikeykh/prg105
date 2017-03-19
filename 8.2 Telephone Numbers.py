# Many companies use telephone numbers like 555-GET-FOOD so
# the number is easier for their customers to remember.
# On a standard telephone the alphabetic letters are mapped
# to numbers in the following fashion:

# A, B, C = 2
# D, E, F = 3
# G, H, I = 4
# J, K, L = 5
# M, N, O = 6
# P, Q, R, S = 7
# T,U, V, = 8
# W, X, Y, Z = 9

# Write a program that asks the user to enter a 10-character
# telephone number in the format XXX-XXX-XXXX.
# The application should display the telephone number
# with any alphabetic characters that appeared in the
# original translated to their numeric equivalent.
# For example, if the user enters 555-GET-FOOD the application
# should display 555-438-3663.

# Use appropriate variables, functions, and comments.
# Upload to GitHub and hand in the link.

# Make a list of all the letters of the alphabet
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Create a list of number that correspond with their assigned letters
num = [2, 2, 2, 3, 3, 3, 4, 4, 4,
       5, 5, 5, 6, 6, 6, 7, 7, 7, 7,
       8, 8, 8, 9, 9, 9, 9]
# Ask the user to enter an alpha-numeric phone number in the correct format
phone = input('Enter an alpha-numeric phone number '
              'in the format XXX-XXX-XXXX : ').lower()

# create an empty string to build the new phone number
s = ""

# create a for loop to convert letter to numbers
# or the numbers original numbers from the input
for i in range(len(phone)):
    if phone[i].isalpha():
        s += str(num[letters.index(phone[i])])
    else:
        s += phone[i]

# print the final string
print(s)
