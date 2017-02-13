# Running on a treadmill you burn 4.2 calories per minute.
# Write a program that uses a loop to display the number of
# calories burned after 10, 15, 20, 25 and 30 minutes.

calories_per_minute = 4.2
for number_of_minutes in range(10, 31, 5):
    calories = (number_of_minutes / 1) * calories_per_minute
    print("If you run on a treadmill for", number_of_minutes, "minutes", "you will burn", calories, "calories.")
