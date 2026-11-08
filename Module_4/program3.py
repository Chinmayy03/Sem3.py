contact={}
while True:
    print("1. Add Contact")
    print("2. View Contact")
    print("3. search Contact")
    print("4. exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        contact[name]=phone
        print("Contact added successfully!")
    elif choice==2:
        if not contact:
            print("No contacts found.")
        else:
            for name, phone in contact.items():
                print(f"Name: {name}, Phone: {phone}")
    elif choice==3:
        search_number=input("Enter phone number to search: ")
        if search_number in contact.values():
            for name, phone in contact.items():
                if phone == search_number:
                    print(f"Name: {name}, Phone: {phone}")
                    break
        else:
            print("Contact not found.")
    elif choice==4:
        print("Exiting the program.")
        break