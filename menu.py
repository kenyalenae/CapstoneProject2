# Create a database menu program that calls out other programs

import sys
from menuOption1 import create_database
from menuOption2 import add_row
from menuOption3 import update_row
from menuOption4 import delete_row
from menuOption5 import display_all
from menuOption6 import display_row


# run the program until the user selects no to end program
def main():
    run_program = True
    while run_program:
        print_menu()
        selection = input()
        run(selection)
        again = input('Would you like to continue? (y/n)')
        if again.lower() == 'n':
            print('Closing program now...')
            run_program = False


# display the menu
def print_menu():
    print(30 * '-', 'DATABASE MENU PROGRAM', 30 * '-')
    print('1: Create a database and a table')
    print('2: Add a row of data')
    print('3: Update a row')
    print('4: Delete a row')
    print('5: Display all rows in table')
    print('6: Display single row of data')
    print('7: Exit program')
    print(60 * '-')
    print('Please select your menu option [1-7]: ')


# depending on user input, run selected menu option
def run(option):

    if option == '1':
        print('You chose option 1: Create a database and a table')
        create_database()
    elif option == '2':
        print('You chose option 2: Add a row')
        add_row()
    elif option == '3':
        print('You chose option 3: Update a row')
        update_row()
    elif option == '4':
        print('You chose option 4: Delete a row')
        delete_row()
    elif option == '5':
        print('You chose option 5: Display all rows in table')
        display_all()
    elif option == '6':
        print('You chose option 6: Display single row of data')
        display_row()
    elif option == '7':
        sys.exit()
    else:
        input('That is not a valid selection. Please enter value between [1-7]: ')


main()
