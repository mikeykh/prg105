# A nutritionist who works for a fitness club helps members by evaluating their diets.
# As part of her evaluation, she asks members for the number of fat grams, carbohydrate grams,
# and protein grams that they consumed in a day.
# Then, she calculates the number of calories that result from the fat, using the following formula:
# calories from fat = fat grams X 9
# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
# calories from carbs = carb grams X 4
# Next, she calculates the number of calories that result from the proteins, using the following formula:
# calories from protein = protein grams X 4

# Use a different function for each nutrient to make calculations by nutrient, and
# print the calories for that nutrient on screen.
# Use a Global variable to accumulate the total calories for the day.
# Add a function to print the total calories for the day.

# Use meaningful names for each variable and function.
# Add a comment to each function describing what it does.


def main():
    # This function asks the user to enter the number of grams of fat, carbs and protein
    # they consumed today. It also calls all of the other functions in the program.
    fat_grams = float(input("Enter the number of fat grams consumed today: "))
    carb_grams = float(input("Enter the number of carbohydrate grams consumed today: "))
    pro_grams = float(input("Enter the number of protein grams consumed today: "))
    calories_from_fat = calc_cals_from_fat(fat_grams)
    calories_from_carbs = calc_cals_from_carbs(carb_grams)
    calories_from_protein = calc_cals_from_pro(pro_grams)
    print_total_cals(calories_from_fat, calories_from_carbs, calories_from_protein)


def calc_cals_from_fat(fat_grams):
    # This functions calculates the number of calories from fat consumed today
    # and returns the amount calculated.
    fat_cals = fat_grams*9
    print("The amount of calories consumed from fat is:", fat_cals)
    return fat_cals


def calc_cals_from_carbs(carb_grams):
    # This functions calculates the number of calories from carbs consumed today
    # and returns the amount calculated.
    carb_cals = carb_grams*4
    print("The amount of calories consumed from carbohydrates is:", carb_cals)
    return carb_cals


def calc_cals_from_pro(pro_grams):
    # This functions calculates the number of calories from protein consumed today
    # and returns the amount calculated.
    pro_cals = pro_grams*4
    print("The amount of calories consumed from protein is:", pro_cals)
    return pro_cals


def print_total_cals(fat_cals, carb_cals, pro_cals):
    # This function calculates the total amount of calories consumed today
    # and prints the value in a meaningful message.
    total_cals = fat_cals + carb_cals + pro_cals
    print("Your daily caloric intake is: ", total_cals)


# This calls the main function.
main()
