def print_menu():
    print('1. Add a Phone Number')
    print('2. Remove a Phone Number')
    print('3. Search a Phone Number')
    print('4. Quit')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Print Phone Numbers")
        name = input("Name: ")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x],"e-mail: ", email[x])
        print()
    elif menu_choice == 2:
        print("Add Name,Number,E-mail")
        name = input("Name: ")
        phone = input("Number: ")
        email = input("E-mail:")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Remove Name and Number,E-mail")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 5:
        print_menu()
    
