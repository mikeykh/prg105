# Write a program that uses nested loops to collect data and calculate
# the average rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate 12 times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.
total_months = 0
total_inches_of_rain = 0
entered_number_of_years = int(input("Please enter the number of years: "))
for current_year in range(1, entered_number_of_years + 1):
    for current_month in range(1, 13):
        monthly_rainfall_inches = float(input("Please enter the inches of " +
                                              "rainfall for month " + format(current_month, "d")+": "))
        total_inches_of_rain += monthly_rainfall_inches
        total_months += 1
average_rainfall = total_inches_of_rain / total_months
print("Number of months: " + format(total_months, "d"),
      "Total inches of rainfall: ", format(total_inches_of_rain, ".2f"),
      "Average rainfall: "+format(average_rainfall, ".2f"), sep="\n")
