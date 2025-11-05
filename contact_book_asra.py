# Contact Organizer by Asra

# List to store all entries
my_contacts = []

# Main menu loop
while True:  # Keep showing menu until user exits
    print("\n=== My Contact Organizer ===")
    print("1. Add New Contact")
    print("2. Show All Contacts")
    print("3. Find Contact")
    print("4. Modify Contact")
    print("5. Remove Contact")
    print("6. Exit Program")
    
    option = input("Choose an option (1-6): ")  # User input

    # Add a new contact
    if option == '1':
        store_name = input("Store Name: ")
        phone_num = input("Phone Number: ")
        email_addr = input("Email: ")
        home_addr = input("Address: ")
        
        entry = {
            "store_name": store_name,
            "phone_num": phone_num,
            "email_addr": email_addr,
            "home_addr": home_addr
        }
        
        my_contacts.append(entry)
        print("✅ Contact added to your organizer!")

    # Show all contacts
    elif option == '2':
        if not my_contacts:
            print("No contacts saved yet.")
        else:
            print("\n--- Your Contacts ---")
            for idx, entry in enumerate(my_contacts, start=1):
                print(f"{idx}. {entry['store_name']} - {entry['phone_num']}")

    # Search for a contact
    elif option == '3':
        query = input("Enter name or phone number to find: ")
        found = False
        for entry in my_contacts:
            if query.lower() in entry['store_name'].lower() or query in entry['phone_num']:
                print(f"Name: {entry['store_name']}, Phone: {entry['phone_num']}, Email: {entry['email_addr']}, Address: {entry['home_addr']}")
                found = True
        if not found:
            print("No matching contact found.")

    # Modify a contact
    elif option == '4':
        query = input("Enter name or phone number to modify: ")
        for entry in my_contacts:
            if query.lower() in entry['store_name'].lower() or query in entry['phone_num']:
                entry['store_name'] = input(f"New name ({entry['store_name']}): ") or entry['store_name']
                entry['phone_num'] = input(f"New phone ({entry['phone_num']}): ") or entry['phone_num']
                entry['email_addr'] = input(f"New email ({entry['email_addr']}): ") or entry['email_addr']
                entry['home_addr'] = input(f"New address ({entry['home_addr']}): ") or entry['home_addr']
                print("✅ Contact updated!")
                break
        else:
            print("No contact found to modify.")

    # Remove a contact
    elif option == '5':
        query = input("Enter name or phone number to remove: ")
        for entry in my_contacts:
            if query.lower() in entry['store_name'].lower() or query in entry['phone_num']:
                my_contacts.remove(entry)
                print("✅ Contact removed from your organizer!")
                break
        else:
            print("No contact found to remove.")

    # Exit program
    elif option == '6':
        print("Exiting Contact Organizer. Bye! 👋")
        break

    # Handle invalid input
    else:
        print("❌ Invalid option. Try again.") 
