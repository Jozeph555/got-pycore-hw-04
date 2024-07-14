"""Main script"""


def parse_input(user_input):
    """Parses the command entered by the user 
    into a command and its arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """Adds a new contact to the 
    contact dictionary"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Changes an existing contact 
    in the contact dictionary"""
    name, phone = args
    if name not in contacts:
        return "There is no such name in contacts"
    contacts[name] = phone
    return "Contact changed."

def show_phone(name, contacts):
    """Outputs the phone number 
    for the specified contact"""
    name = name[0]
    if name not in contacts:
        return "There is no such name in contacts"
    return contacts[name]

def show_all(contacts):
    """Outputs all saved contacts 
    with phone numbers"""
    return contacts


def main():
    """Main function"""

    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            all_contacts = show_all(contacts)
            for name, phone in all_contacts.items():
                print(f"{name}: {phone}")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
