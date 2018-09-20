# When user selects option 5
# allow user to display all rows in table

import sqlite3


# function to display all rows in table
def display_all():

    sqlite_file = 'test1_db.sqlite'
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)

    # display information for all employees
    for row in conn.cursor().execute('SELECT * FROM EMPLOYEE_TEST'):
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("CITY = ", row[3])
        print("STATE = ", row[4])
        print("ZIP CODE = ", row[5])
        print("SALARY = $", row[6], "\n")

    conn.commit()
    print("Records displayed successfully")
    conn.close()


