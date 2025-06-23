

def add_contact(contacts):
    """
    Function adds the name and number in the (contacts)dictionary.
    returns:
        str: added messsage or already exists
    """

    name = input("Name:")
    if name in contacts:     # checking name in contacts
        print('contact already Exists')
    else:
        number = input('Phone number: ')
        contacts[name] = number  # assigning vlaue to the key
        print('contact added')

def search_contact(contacts):

    """
    Funtions finds the contact in dictionary
    Returns:
        str: Name and contact info  or not found
    """
    name = input('Name: ') 
    if name in contacts:    # checking name in contacts
        print(f'{name}: {contacts[name]}')
    else:
        print('contact not found')

def delete_contact(contacts):

    """
    Funtion deletes the contact
    Returns:
        str: contact deleted message or not found
    """

    name = input('Name: ')
    if name in contacts:    # checking name in contacts
        del contacts[name]
        print('contact deleted')
    else:
        print('contact not found')

def update_contact(contacts):

    """
    Function updates the contact
    Returns: 
        str: contact updated or not found
    """

    name = input("Name: ") 
    if name in contacts:
        number = input("phone number: ")
        contacts[name] = number
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_contact(contacts):
    """
    Function display all contacts
    returns:
        str: Contact info
    """

    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for name, number in contacts.items():
            print(f"{name}: {number}")


# main function 
if __name__ == "__main__":

    contacts = {}   # contact dictionary

    while True:
        print()
        print("=====Contact List manager=====")
        print('1. Add Contact\n2. delete_contact\n3. update_contact\n4. show_contact\n5. Search contact\n6. Exit')
        choice = int(input("Enter Choice: "))
        
        # user choice
        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            delete_contact(contacts)
        elif choice == 3:
            update_contact(contacts)
        elif choice == 4:
            show_contact(contacts)
        elif choice==5:
            search_contact(contacts)
        elif choice == 6:
            print('Exiting Byee')
            break
        else:
            print("Enter valid input")


