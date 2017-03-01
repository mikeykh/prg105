# Copy your file from the previous exercise (Average numbers)
# and modify it so that it handles the following exceptions:
# It should handle any IOError exceptions that are
# raised when the file is opened and data is read from it.
# It should handle any ValueError exceptions that are
# raised when the items that are read from the file are converted to a number.
# Upload your .py file on GitHub and hand in the link to the file.


def main():
    # This function opens the file numbers.txt
    # and calculates the average of all the numbers within it
    # and prints a meaningful message.
    divisor = 18
    total = 0
    average = 0
    try:
        # Checks to see if there are any exceptions
        numbers_file = open("numbers.txt", "r")
        for count in range(1, 19):
            divisor += 1
        for line in numbers_file:
            total += (int(line))
            average = total/18
    except Exception as err:
        # If an exception occurred, an error message will be printed
        print(err)
    else:
        # If no exceptions occurred, the program will print
        # the contents of the file and a meaningful message
        # regarding the average of the numbers.
        print(numbers_file.read())
        numbers_file.close()
        print("The average of the numbers in this list is: ", average)


main()
