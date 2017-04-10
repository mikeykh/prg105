# In this programming exercise you will create a simple trivia game for two players. The program will work like this:

# Starting with player 1, each player gets a turn at answering 5 trivia questions.
# (There should be a total of 10 questions.) When a question is displayed, 4 possible answers are also displayed.
# Only one of the answers is correct, and if they player selects the correct answer, he or she earns a point.
# After answers have been selected for all the questions, the program displays
# the number of points earned by each player and declares the player with the highest number of points the winner.
# To create this program, write a Question class to hold the data for the trivia question.

# The question class should have attributes for the following data:
# A trivia question
# Possible answer 1
# Possible answer 2
# Possible answer 3
# Possible answer 4
# The number of the correct answer (1, 2, 3, or 4)
# The Question class should also have an appropriate __init__ method, accessors, and mutators.

# The program should have a list or a dictionary containing 10 Question Objects, one for each trivia question.
# Make up your own trivia question on the subject or subjects of your choice for the objects.

# Document appropriately with comments, upload to GitHub and hand in the link to your file.


import question as qu
from random import shuffle

qlist = []

# Create questions objects
q1 = qu.Question("Babe Ruth is associated with which sport?: ",
                 "A. Football", "B. Tennis", "C. Baseball", "D. Golf", "C")

q2 = qu.Question("How many Wonders of the World are there?: ",
                 "A. 5", "B. 6", "C. 7", "D. 8", "C")

q3 = qu.Question("What color is the circle on the Japanese national flag?: ",
                 "A. Blue", "B. Red", "C. Green", "D. Yellow", "B")

q4 = qu.Question("What is the chemical symbol for Hydrogen?: ",
                 "A. Hi", "B. Hy", "C. H", "D. Hg", "C")

q5 = qu.Question("How many sides does an octagon have?: ",
                 "A. Five", "B. Six", "C. Seven", "D. Eight", "D")

q6 = qu.Question("The Walker Cup is competed for in which sport?: ",
                 "A. Football", "B. Tennis", "C. Baseball", "D. Golf", "D")

q7 = qu.Question("What is the postal abbreviation for Idaho?: ",
                 "A. DA", "B. ID", "C. IH", "D. IO", "B")

q8 = qu.Question("How many players make up a Basketball team?: ",
                 "A. Five", "B. Six", "C. Seven", "D. Eight", "A")

q9 = qu.Question("Which has the highest mountain: Earth or Mars?: ",
                 "A. Earth", "B. Mars", "C. Both", "D. Neither", "B")

q10 = qu.Question("Michael Jordan gave up basketball to try which sport in 1993?: ",
                  "A. Football", "B. Tennis", "C. Baseball", "D. Golf", "C")

# List that holds all of the questions
qlist.extend((q1, q2, q3, q4, q5, q6, q7, q8, q9, q10))

# Shuffle the list so questions are in a different order every time the program runs
shuffle(qlist)

# Setting up point values for players
p1_score = 0
p2_score = 0

# Setting question number for while loops
qnum = 0

# For player one
print("=================")
print("= Player 1: Go! =")
print("=================\n")
while qnum < 5:
    # ask question (from list)
    print("Question " + str(qnum+1))
    print(qlist[qnum].__str__())
    # Set user input answer
    x = input("Type the letter of your guess: ")
    qlist[qnum].set_user_ans(x)
    # Check  user answer is correct
    y = qlist[qnum].get_user_ans()
    z = qlist[qnum].get_correct_ans()
    if y[0].lower() == z[0].lower():
        p1_score += 1
        print("$$$$CA-CHING$$$ CORRECT\n")
    else:
        print("guess what, WRONG!\n")
    # Increment counter
    qnum += 1

# For player two
print("\n=================")
print("= Player 2: Go! =")
print("=================\n")
while 5 <= qnum < 10:
    # ask question (from list)
    print("Question " + str(qnum-4))
    print(qlist[qnum].__str__())
    # Set user input answer
    x = input("Type the letter of your guess: ")
    qlist[qnum].set_user_ans(x)
    # Check  user answer is correct
    y = qlist[qnum].get_user_ans()
    z = qlist[qnum].get_correct_ans()
    if y[0].lower() == z[0].lower():
        p2_score += 1
        print("$$$$CA-CHING$$$ CORRECT\n")
    else:
        print("guess what, WRONG\n")
    # Increment counter
    qnum += 1

# Players' scores
print("\n=============")
print("= Scores! =")
print("=============\n")

print("Player 1: " + str(p1_score))
print("Player 2: " + str(p2_score) + "\n")

# Compare p1 and p2
if p1_score > p2_score:
    print("Player 1 wins, Player 2 Loses")
elif p1_score < p2_score:
    print("Player 2 Wins, Player 1 Loses")
else:
    print("Oops, it's a tie")
