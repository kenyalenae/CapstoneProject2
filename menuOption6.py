# When user selects option 6
# allow user to display a row in table

import sqlite3


# display one row only
def display_row():

    sqlite_file = 'test1_db.sqlite'
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)

    # ask user for id of employee they would like to view
    choice = input('Please enter employee ID of the employee you would like to view: ')

    # display all info for the selected employee
    for row in conn.cursor().execute('SELECT * FROM EMPLOYEE_TEST WHERE ID =?', (choice,)):
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("CITY = ", row[3])
        print("STATE = ", row[4])
        print("ZIP CODE = ", row[5])
        print("SALARY = $", row[6], "\n")

    conn.commit()
    print("Record displayed successfully")
    conn.close()

