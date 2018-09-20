# When user selects menu option 2
# Create a row of data

import sqlite3


# add row of data to table
def add_row():

    # ask user for input
    employee_id = int(input('Enter employee ID: '))
    employee_name = input('Enter employee name: ')
    address = input('Enter street address: ')
    city = input('Enter city: ')
    state = input ('Enter state: ')
    zip_code = int(input('Enter zip code: '))
    salary = int(input('Enter employee salary: '))

    add_to_db(employee_id, employee_name, address, city, state, zip_code, salary)


# function to add row depending on user's input
def add_to_db(employee_id, employee_name, address, city, state, zip_code, salary):

    sqlite_file = 'test1_db.sqlite'
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # insert data from user input into table
    c.execute('INSERT INTO EMPLOYEE_TEST VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (employee_id, employee_name, address, city, state, zip_code, salary))

    conn.commit()
    print("Records created successfully")
    conn.close()



