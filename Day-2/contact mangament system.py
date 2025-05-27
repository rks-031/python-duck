# Functionalities:
# Add a new contact
# View all contacts
# Search for a contact
# Update a contact
# Delete a contact
# Exit the program

def add_new_contact(contacts):
    name = input("Enter the contact name:")
    phone = input("Enter the contact phone number:")
    email = input("Enter the contact email:")
    if email in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {'email': email, 'phone' : phone}


def view_all_contacts(contacts):
    if(not contacts):
        print("No contacts available.")
    else:
        print("Contacts are:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def search_contact(contacts, name):
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("Contact not found.")

def update_contact(contacts,name):
    print(f"For the user, {name}, what do you wish to update?")
    print("1. Phone Number")
    print("2. Email")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        new_phone = input("Enter the new phone number:")
        contacts[name]['phone'] = new_phone
    elif choice == '2':
        new_email = input("Enter the new email:")
        contacts[name]['email'] = new_email
    
def delete_contact(contacts,name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def operations(contacts, user_choice):
    if user_choice == '1':
        add_new_contact(contacts)
    elif user_choice == '2':
        view_all_contacts(contacts)
    elif user_choice == '3':
        name = input("Enter the name of the contact to search:")
        search_contact(contacts,name)
    elif user_choice == '4':
        update_contact(contacts)
    elif user_choice == '5':
        delete_contact(contacts)
    elif user_choice == '6':
        print("Exiting the program. Goodbye!")
        exit()

def main():
    print("Welcome to the Contact Management System")
    contacts = {}
    choice = 'Y'
    while(choice == 'Y' or choice == 'y'):
        print("\nMenu:")
        print("1. Add a new contact")  
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")
        user_choice = input("Please enter your choice (1-6): ")
        operations(contacts, user_choice)
        choice = input("Do you want to continue? (Y/N): ")

if __name__ == "__main__":
    main()