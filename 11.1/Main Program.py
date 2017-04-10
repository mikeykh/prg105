# imports the desk method
import desk


def main():
    # initialize using the Desk class from the desk module
    product_info = desk.Desk("Desk", "Balsa", "7ft", "3ft", "3ft", 699.99, "Right", 2)

    # Prints the information
    print(product_info)


main()
# call the main function
