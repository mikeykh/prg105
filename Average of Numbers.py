# Write a program that uses the numbers.txt file,
# which contains a series of integers.
# Your program will calculate the average of all of the numbers
# stored in the file and display the total on the screen.
# Use appropriate variables, functions, and comments.
# Upload your .py file to GitHub and hand in the link.


def main():
    divisor = 18
    total = 0
    average = 0
    numbers_file = open("numbers.txt", "r")
    for count in range(1, 19):
        divisor += 1
    for line in numbers_file:
        total += (int(line))
        average = total/18
    print(numbers_file.read())
    print("The average of the numbers in this list is: ", average)


main()
