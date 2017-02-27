# Write a program that asks a user to enter 5 test scores, and store them in variables.
# Write the following functions:
# calc_average - This function should accept five
# test scores as arguments and return the average of the scores.
# determine_grade - This function should accept the average
# of the test scores as an argument and return a letter grade based on the following scale:

# Score	Letter Grade
# 90-100	A
# 80-89	B
# 70-79	C
# 60-69	D
# Below 60	F

# Properly name variables, use comments, upload to GitHub, hand in link.


def main():
    # This function calls all of the other functions in the program
    # and prints out the users average letter grade.
    print("This program will ask you to enter five test score and it will give you your average letter grade.")
    (score1, score2, score3, score4, score5) = input_score()
    grade_average = calc_average(score1, score2, score3, score4, score5)
    print("Your average letter grade is a(n):", determine_grade(grade_average))


def input_score():
    # This function accepts input from the user
    # and returns each input as a variable.
    score1 = float(input("Enter your first score: "))
    score2 = float(input("Enter your second score: "))
    score3 = float(input("Enter your third score: "))
    score4 = float(input("Enter your fourth score: "))
    score5 = float(input("Enter your fifth score: "))
    return score1, score2, score3, score4, score5


def calc_average(score1, score2, score3, score4, score5):
    # This function calculates the average of five score that were
    # input by the user and returns it as a variable.
    average = (score1 + score2 + score3 + score4 + score5)/5
    return average


def determine_grade(average):
    # This function determines the letter grade of the users average grade
    # and returns it.
    if average < 60:
        return "F"
    elif average < 70:
        return "D"
    elif average < 80:
        return "C"
    elif average < 90:
        return "B"
    elif average < 101:
        return "A"
    else:
        return "Error"


# Calls the main function
main()
