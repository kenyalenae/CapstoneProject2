# When user selects option 4
# allow user to delete a row

import sqlite3


# function to delete a row of data depending on user input
def delete_row():

    sqlite_file = 'test1_db.sqlite'
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # ask user for id of employee they would like to delete
    x = input('Enter the ID of the employee you would like to delete: ')

    # delete row depending on user input
    c.execute('DELETE FROM EMPLOYEE_TEST WHERE EMP_ID =?', (x,))

    conn.commit()
    print("Records deleted successfully")
    conn.close()


