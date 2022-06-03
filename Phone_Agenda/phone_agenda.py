

file_name = "E:\Python it-school\Phone_Agenda\phone_agenda.txt"
file1 = open(file_name, "a+")


def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print("\n   *** Phone Book Menu ***\n"+
          "Enter 1,2,3 or 4:\n"+
          "Enter 1 To Display Your Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To search your contacts\n"+
          "Enter 4 To Quit\n**********************")
    choice = input("Enter your choice: ")
    if choice == "1":
        file1 = open(file_name, "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Agenda is empty")
        else:
            print (file_contents)
        file1.close
        ret_to_main_menu_prompt()
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        ret_to_main_menu_prompt()
        enter_contact_record_again()
        ret_to_main_menu_prompt()
    elif choice == "3":
        search_contact_record()
        ret_to_main_menu_prompt()
        show_main_menu()
    elif choice== "4":
        print("Thanks for using Phone Agenda")
    else:
        print("Wrong choice, Please Enter [1 to 4]\n")
        ret_to_main_menu_prompt()
        show_main_menu()
        
def search_contact_record():
    ''' This function is used to searches a specific contact record '''
    search_name = input("Enter first and last name for Searching contact record: ")
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            print (line)
            found=True
            break
    if  found == False:
        print("There's no contact Record in your Agenda with name = " + search_name )

def input_firstname():
    ''' First name '''
    first_name = input("Enter First name ")
    return first_name

def input_lastname():
    ''' Last name '''
    last_name = input("Enter Last name ")
    return last_name


def enter_contact_record():
    ''' It  collects contact info first name, last name, email and phone '''
   
    first = input_firstname()
    last = input_lastname()
    phone = input('Enter Phone number ')
    email = input('Enter E-mail ')
    contact = ("+-----------------------------+\n" + 
    "First name: " + first + "\n" +
    "Last name: " + last + "\n " +
    "Phone number: " + phone + "\n" +
    "Email: " + email +  "\n" +
    "+-----------------------------+\n")
    file1 = open(file_name, "a")
    file1.write(contact)
    print( "This contact\n " + contact + "has been added successfully!")
    
def enter_contact_record_again():
    '''Ask if you want to add another contact or not'''
    print ("[Enter 1 or 2]\n"+
    "Enter 1 to add another contact\n"+
    "Enter 2 if you dont't want to add another contact"
    )
    choice = input("Enter your choice: ")
    if choice == "1":
        enter_contact_record()
        ret_to_main_menu_prompt() 
        enter_contact_record_again()
    elif choice == "2":
        show_main_menu()

def ret_to_main_menu_prompt():
    input("Press Enter to continue ...") 


show_main_menu()