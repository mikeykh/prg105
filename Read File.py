# Download the file names.txt
# Save it into the same project folder in pycharm
# that you are using for this project.
# Your Python file will:
# Read and Display the list of names from the file
# Display the number of names that are read from the file

# (You will need a variable to keep a count of
# the number of items read from the file.)
# Use functions and variables with appropriate names and comments.
# Upload the .py file to GitHub and hand in the link.


def main():
    number = 0
    names_file = open("names.txt", "r")
    for count in range(1, 23):
        number += 1
    print(names_file.read())
    print("The number of names in this list is: ", number)


main()
