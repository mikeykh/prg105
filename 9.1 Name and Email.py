# Write a program that keeps names and email addresses in a dictionary as key-value pairs.
# The program should display a menu that lets the user look up a person's email address,
# add a new name and email address, change an existing email address,
# and delete an existing name and email address. The program should pickle the dictionary and
# save it to a file when the user exits the program. Each time the program starts,
# it should retrieve the dictionary from the file and unpickle it.

# Use separate functions, upload both the created file and the program to GitHub.
# Submit link to .py file and add a link to the text file in the comments.

import pickle as pik


def check():
    try:
        cont_file = open("Contacts.dat", "rb")
        cont_set = pik.load(cont_file)
        cont_file.close()
        if cont_set == {}:
                print("You have no contacts.")
        else:
            return cont_set
    except EOFError:
        print("You have no contacts.")
        return
    except FileNotFoundError:
        print("You have no contacts.")
        return


def look_up():
    print("\nSEARCH CONTACTS\n")
    cont_set = check()
    if cont_set is None:
        return
    else:
        try:
            search = input("Enter contact name, or 'Menu': ")
            if search.lower() == 'Menu':
                return
            elif search.lower() == 'all':
                for key, value in sorted(cont_set.items()):
                    print("Name: ", key, "\nEmail:", value, "\n")
                return
            else:
                print("Name: ", search, "\nEmail:", cont_set[search])
                return
        except KeyError:
            print("Entry does not exist.")


def add():
    print("\nADD CONTACT\n")
    try:
        cont_file = open("Contacts.dat", "rb")
        cont_set = pik.load(cont_file)
        cont_file.close()
        new_cont = input("Enter contact name or 'Menu': ")
        if new_cont.lower() == 'menu':
            return
        else:
            cont_email = input("Enter contact e-mail: ")
            cont_set.update({new_cont: cont_email})
            cont_file = open("Contacts.dat", "wb")
            pik.dump(cont_set, cont_file)
            cont_file.close()
    except EOFError:
        print("You have no contacts")
        new_cont = input("Enter contact name or 'Menu': ")
        if new_cont.lower() == 'menu':
            return
        else:
            cont_email = input("Enter contact e-mail: ")
            cont_set = {}
            cont_set.update({new_cont: cont_email})
            cont_file = open("Contacts.dat", "wb")
            pik.dump(cont_set, cont_file)
            cont_file.close()
            return
    except FileNotFoundError:
        print("The data file does not exist. "
              "\nAdd a contact to create the data file.")
        new_cont = input("Enter contact name or 'Cancel': ")
        if new_cont.lower() == 'cancel':
            return
        else:
            cont_email = input("Enter contact e-mail: ")
            cont_set = {}
            cont_set.update({new_cont: cont_email})
            contact_file = open("Contacts.dat", "wb")
            pik.dump(cont_set, contact_file)
            contact_file.close()
            return


def edit_cont():
    print("\nEDIT CONTACT\n")
    cont_set = check()
    if cont_set is None:
        return
    else:
        edit = input("Enter contact name or 'Menu': ")
        if edit.lower() == 'menu':
            return
        else:
            new_email = input("Enter new e-mail or 'Menu': ")
            if new_email.lower() == 'menu':
                return
            else:
                cont_set[edit] = new_email
                print("Name:     ", edit, "\nNew Email:", cont_set[edit])
                cont_file = open("Contacts.dat", "wb")
                pik.dump(cont_set, cont_file)
                cont_file.close()
                return


def delete():
    print("\nDELETE CONTACT\n")
    cont_set = check()
    if cont_set is None:
        return
    else:
        try:
            remove = input("Enter contact name or 'Menu': ")
            if remove.lower() == 'menu':
                return
            else:
                cont_set.pop(delete)
                print(delete, "has been removed from your contacts list.")
                cont_file = open("Contacts.dat", "wb")
                pik.dump(cont_set, cont_file)
                cont_file.close()
                if cont_set is None:
                    print("You have no contacts.")
                else:
                    return
        except KeyError:
            print("Entry does not exist.")
            return


def view_all():
    contact_set = check()
    if contact_set is None:
        return
    else:
        for key, value in sorted(contact_set.items()):
            print("Name: ", key, "\nEmail:", value, "\n")
            return


def save_quit():
    cont_set = check()
    if cont_set is None:
        return
    else:
        cont_file = open("Contacts.dat", "wb")
        pik.dump(cont_set, cont_file)
        cont_file.close()
        return


def main_menu():
    choice = ""
    while choice.lower() != "quit":
        print("\n      MAIN MENU      \n")
        choice = input("Choose an option (Number):\n"
                       "1. Add Contact\n"
                       "2. Search Contact\n"
                       "3. Edit Contact\n"
                       "4. Delete Contact\n"
                       "5. View All\n"
                       "6. Save and Quit\n\n")
        if choice.lower() in "1":
            add()
        elif choice.lower() in "2":
            look_up()
        elif choice.lower() in "3":
            edit_cont()
        elif choice.lower() in "4":
            delete()
        elif choice.lower() in "5":
            view_all()
        elif choice.lower() in "6":
            save_quit()
            break
        else:
            print("Your input is invalid.")


main_menu()

