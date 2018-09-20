# When user selects option 3
# allow user to update a row

import sqlite3


# function to update row
def update_row():

    sqlite_file = 'test1_db.sqlite'
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # ask user for id of employee they would like to update
    x = input('Please enter ID of employee you would like to update: ')

    # print menu for choices of which columns they can choose to update
    print('Here are the columns you can update: ')
    print('1: EMP_NAME')
    print('2: ADDRESS')
    print('3: CITY')
    print('4: STATE')
    print('5: ZIP_CODE')
    print('6: SALARY')
    y = input('Which column would you like to update?: ')

    # update the column with users input depending on which option the user chooses
    if y == '1':
        new_name = input('Enter employees new name: ')
        c.execute('UPDATE EMPLOYEE_TEST SET EMP_NAME =? WHERE ID =?', (new_name, x,))

    elif y == '2':
        new_add = input('Enter employees new address: ')
        c.execute('UPDATE EMPLOYEE_TEST SET ADDRESS =? WHERE ID =?', (new_add, x,))

    elif y == '3':
        new_city = input('Enter employees new city: ')
        c.execute('UPDATE EMPLOYEE_TEST SET CITY =? WHERE ID=?', (new_city, x,))

    elif y == '4':
        new_state = input('Enter employees new state: ')
        c.execute('UPDATE EMPLOYEE_TEST SET STATE =? WHERE ID=?', (new_state, x,))

    elif y == '5':
        new_zip = input('Enter employees new zip code: ')
        c.execute('UPDATE EMPLOYEE_TEST SET ZIP_CODE =? WHERE ID=?', (new_zip, x,))

    elif y == '6':
        new_sal = input('Enter employees new salary: ')
        c.execute('UPDATE EMPLOYEE_TEST SET SALARY =? WHERE ID=?', (new_sal, x,))

    else:
        input('That is not a valid selection. Please enter value between [1-6]: ')

    conn.commit()
    print("Records updated successfully")
    conn.close()

