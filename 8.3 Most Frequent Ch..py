# Write a program that lets the user enter a string and
# displays the character that appears most frequently in the string.
# Use appropriate variables, functions, and comments.
# Upload to GitHub and hand in link.


# This function creates a list of of any size where the elements are all 0
def create_ist(e):
    lst = []
    for ind in range(e):
        lst.append(0)
    return lst

# Creates a list with 26 elements
alphaCount = create_ist(26)

# Gather string from user
user_string = input("In one sentence, what is your favorite holiday?: ")

# String variable with letters of alphabet
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Finds the amount of all the letters of the alphabet that the user string contains
for i in user_string:
    ch = i.upper()
    index = Alpha.find(ch)
    if index > -1:
        alphaCount[index] += 1

max_value = (max(alphaCount))
index_of_max = (alphaCount.index(max_value))
most_frequent = (Alpha[index_of_max])
print("The most frequent character in your sentence is: ", most_frequent, '.', sep='')
