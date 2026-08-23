
def menu():
    print("1: add a contact")
    print("2: show contacts")
    print("3: remove a contact")
    print("4: exit")

def run():
    print("welcome to your contact management program !")
    while True:
        menu()
        userInput = input("choose ====>");
        match userInput:
            case "1":
                addContact()
            case "2":
                getAllContacts()
            case "3":
                removeContact()
            case "4":
                # sys.exit()
                break
            case _ :
                print("---------------choice invalid---------------")





# create
def addContact():
    name = input("enter the name: ")
    email = input("enter the email: ")
    num = input("enter the phone number: ")
    createContact(name,email,num)
    print("contact created successfully")
    
def createContact(name,email,num):
    with open("contacts.txt", "a", encoding= "utf-8") as file:
        file.write(f"name: {name} | email: {email} | phone number: {num}\n")


# Read 
def getAllContacts():
    try:
        with open("contacts.txt", "r", encoding= "utf-8") as file:
            contacts = file.readlines()
    except FileNotFoundError:
        print("contact text file doesnt exist")
        return False
    if not contacts:
        print("no contacts found")
        return False
    for number,contact in enumerate(contacts, start=1):
        print(number, " ==> ", contact)


# delete
def removeContact():
    if not getAllContacts()
        return
    num = input("enter the contact number in order to remove it or 0 to exist: ")
    while num != "0" and not deleteContact(num) :
        getAllContacts()
        num = input("type an existing number or 0 to return to menu: ")


def deleteContact( contactNum ):
    with open("contacts.txt", "r", encoding= "utf-8") as file:
        contacts = file.readlines();
    try:
        del contacts[int(contactNum)-1]
    except Exception :
        print("the number u choosed is not in the list!")
        return False
    
    with open("contacts.txt", "w", encoding="utf-8") as file:
        file.writelines(contacts)
    print ("contact deleted successfully")
    return True






if __name__ == "__main__":
    run()