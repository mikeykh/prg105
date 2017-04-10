# Design a class that holds the following personal data:
# name, address, age, and phone number.
# Write appropriate accessor and mutator methods (get and set).
# Also, write a program that creates three instances of the class.
# One instance should hold your information and
# the other two should hold your friends or family members' information.
# Make sure that each program / class has appropriate comments.
# Upload to GitHub and hand in the link to the program.

import PersonalInfo as Pi


# Main Program creates three instances of the PersonalInfo class and displays them.
def main():

    my_info = Pi.PersonalInfo("Michael Harris", "3022 S Country Club Rd.", 19, "815-575-6273")
    friend_info = Pi.PersonalInfo("Maddy Padjen", "6705 Rode Rd.", 20, "212-888-3489")
    fam_info = Pi.PersonalInfo("Gwen Harris", "3022 S Country Club", 51, "732-709-3409")

    print(my_info.__str__())
    print(friend_info.__str__())
    print(fam_info.__str__())


# calls main function
main()
