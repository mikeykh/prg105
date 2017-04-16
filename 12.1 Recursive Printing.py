# Design a recursive function that accepts an integer argument, n, and prints the numbers 1 up through n


def main():
    # sets the variable n to the number entered by the user
    n = int(input("Enter how many numbers you want to see in sequential order starting from 1: "))

    # passes the the number entered by the user, plus 1, as an argument
    numbers(n+1)


def numbers(times):
    # accepts an argument and prints the numbers from 1 to the argument in sequential order
    for num in range(1, times):
        print(num)

# calls the main function
main()
