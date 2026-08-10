
contact = {}

def menu():
    print("""        CONTACT BOOK
    1. ADD A CONTACT
    2. VIEW CONTACTS
    3. SEARCH FOR A CONTACT
    4. QUIT \n""")

def user_input():
    while True:
        choice = input("Select a choice between 1-4: ")
        if not choice.isdigit():
            print("Enter a choice between 1 and 4\n")
            continue
        choice = int(choice)
        if 1 <= choice <= 4:
            return choice
        print("Enter a choice between 1 and 4\n")

def number_validate():
    while True:
        number = input("Enter a number: ")
        if not number.isdigit():
            print("Enter a valid number \n") 
        else:
            break
    return number

def contact_add(contact):
    name = input("Enter a name: ")
    number = number_validate()
    if name in contact:
         print("Name already exists\n")
    else:
         contact[name] = number

def contact_check(contact):
    name = input("Enter a name: ")
    if name in contact:
        return contact[name]    
    return "Contact not found"


def main():

    while True:
        print()
        menu()
        case = user_input()

        match case:
            case 1:
                contact_add(contact)

            case 2:
                for k,v in contact.items():
                    print(f"{k} : {v}")

            case 3:
                print(contact_check(contact))

            case 4:
                break

if __name__ == "__main__":
    main()




    







    








