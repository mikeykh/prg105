# Write a program that reads the contents of the
# two files into two separate lists.
# The user should be able to enter a boy's name,
# a girl's name, or both and the application
# will display messages indicating whether the names
# were among the most popular.

# Use appropriate functions, comments and variables.
# Upload .py file to GitHub and submit a link to your file.


def main():
    boy_lst = boy_names()
    girl_lst = girl_names()
    names_lst = con_lst(boy_lst, girl_lst)

    yes = input("Do you want to check and see if a name is in the list of most popular names? " + "\n"
                "(Enter 'y' for yes): ")
    while yes == "y":
            name = input("Enter a boy or a girls name: ")
            upper = name.title()
            if upper in names_lst:
                print(upper, "was found in the list of most popular names!")
                again = input("Do you want to check a different name?: " + "\n"
                              "(Enter 'y' for yes): ")
                if again != "y":
                    break
            else:
                print(upper, "was not in the list of most popular names.")
                again = input("Do you want to check a different name? " + "\n"
                              "(Enter 'y' for yes): ")
                if again != "y":
                    break


def boy_names():
    boy_file = open("BoyNames.txt", "r")
    boy_lst = boy_file.readlines()
    boy_file.close()
    return boy_lst


def girl_names():
    girl_file = open("GirlNames.txt", "r")
    girl_lst = girl_file.readline()
    girl_file.close()
    return girl_lst


def con_lst(boy_lst, girl_lst):
    all_names = []
    all_names.extend(boy_lst)
    all_names.extend(girl_lst)
    i = 0
    while i < len(all_names):
        all_names[i] = all_names[i].rstrip("\n")
        i += 1
    tup_names = tuple(all_names)
    return tup_names


main()
