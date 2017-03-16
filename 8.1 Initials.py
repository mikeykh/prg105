# Write a program that gets a string from the user containing
# a person's first, middle, and last names and then displays
# their first, middle, and last initials.

# For example, if the user enters John William Smith,
# the program should display J. W. S.

# Use appropriate functions, names and comments.
# Upload to Github and hand in the link.


def main():
    # Get the user's full name
    my_string = input("Enter in your First, Middle and last name: ")
    # Create a list of the words in my_string
    word_list = my_string.split()
    # Create a for loop to capitalize the for character in each word
    # and print it with a period and a space between each capital letter
    for ch in word_list:
        print(ch[0].upper()+". ", end='')


main()
