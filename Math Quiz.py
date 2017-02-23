# Write a program that gives simple math quizzes.
# The program should display two random numbers that are to be added, such as:
# 247+129

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect, a message showing the correct answer should be displayed.

# Use a function to present the quiz question and get the student answer
# Use a second function to determine if the answer is correct and display the response
# Use meaningful names for functions and variables, use at least one comment for each function to explain what it does.
import random

num1 = random.randint(1, 250)
num2 = random.randint(1, 250)


def question():
    global num1
    global num2
    response = int(input("What is " + str(num1) + " + " + str(num2) + "?:"))
    return response


def check(response):
    global num1
    global num2
    correct_answer = num1+num2
    print()
    if response == correct_answer:
        print("Congratulations!")
    else:
        print("Sorry. The correct answer is", correct_answer)


def main():
    response = question()
    check(response)
main()
