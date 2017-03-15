# Design a program that lets the user enter the
# total rainfall for each of 12 months into a list.
# The program should calculate and display the
# total rainfall for the year, the average monthly rainfall,
# and the months with the highest and lowest amounts.
# Use appropriate functions, variables, and comments.
# Upload your .py file to GitHub and hand in a link to the file.


def get_rainfall(months):
    # Ask the user to enter the inches of rainfall for each month of the year.
    inches_rainfall = []
    for i in range(len(months)):
        monthly_rainfall_inches = float(input("Please enter the inches of rainfall for the month of " + months[i] + ": "))
        inches_rainfall.append(monthly_rainfall_inches)
    return inches_rainfall


def total_rainfall(inches_rainfall):
    # Get the sum rainfall for the year.
    total = 0
    for i in range(len(inches_rainfall)):
        total += inches_rainfall[i]
    return total


def avg_rainfall(total):
    # Calculate the average rainfall for the year.
    average_rainfall = format(total/12, ".2f")
    return average_rainfall


def max_rainfall(inches_rainfall):
    # Check the list for the month with the most rainfall.
    highest_rainfall = max(inches_rainfall)
    return highest_rainfall


def min_rainfall(inches_rainfall):
    # Check the list for the month with the least rainfall.
    lowest_rainfall = min(inches_rainfall)
    return lowest_rainfall


def main():
    # Create a list of every month to be used in a for loop in the function get_rainfall.
    # and display all of the other data calculated within each function. 
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    inches_rainfall = get_rainfall(months)
    total = total_rainfall(inches_rainfall)
    avg_fall = avg_rainfall(total)
    high_rain = max_rainfall(inches_rainfall)
    low_rain = min_rainfall(inches_rainfall)
    highest_rainfall = inches_rainfall.index(high_rain)
    lowest_rainfall = inches_rainfall.index(low_rain)
    print("\nTotal rainfall: ", total, " inches",
          "\nAverage rainfall: ", avg_fall, " inches",
          "\nMonth with max rainfall: ", months[highest_rainfall], " with ", high_rain, " inches",
          "\nMonth with min rainfall: ", months[lowest_rainfall], " with ", low_rain, " inches", sep="")

main()
