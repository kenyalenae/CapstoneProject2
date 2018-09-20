# When user selects menu option 1
# Create a database and table

import sqlite3


# create a database with a pre-defined table
def create_database():

    sqlite_file = 'test1_db.sqlite'    # name of the sqlite database file
    # table_name = input('What would you like to name the table? ')  # ask user what they would like table to be named
    # emp_id = 'Employee ID'  # Employee ID column PRIMARY KEY
    # emp_name = "Name"  # Name of employee
    # address = 'Address Line 1'  # Column for address
    # address2 = 'Address Line 2'  # Optional column for address
    # city = 'City'  # Column for address: city
    # state = 'State'  # Column for address: state
    # zip_code = 'Zip Code'  # Column for address: zip code
    # field_type = 'INTEGER'  # column data type
    # field_type2 = 'TEXT'  # column data type

    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # Creating a second table with 1 column and set it as PRIMARY KEY
    # note that PRIMARY KEY column must consist of unique values!
    # c.execute('CREATE TABLE {tn} ({ei} {ft} PRIMARY KEY) ({en} {ft2}) ({ad1} {ft2})'
    #           '({ad2} {ft2}) ({ct} {ft2}) ({st} {ft2}) ({zc} {ft})'
    #           .format(tn=table_name, ei=emp_id, en=emp_name, ad1=address,
    #                   ad2=address2, ct=city, st=state, zc=zip_code, ft=field_type, ft2=field_type2))

    c.execute('''CREATE TABLE EMPLOYEE_TEST
             (ID            INT PRIMARY KEY    NOT NULL,
             EMP_NAME       TEXT        NOT NULL,
             ADDRESS        CHAR(30)    NOT NULL,
             CITY           CHAR(20)    NOT NULL,
             STATE          CHAR(2)     NOT NULL, 
             ZIP_CODE       INT         NOT NULL,     
             SALARY         REAL);''')

    # Let user know the database/table was created successfully
    print('You have successfully created a database with a table named EMPLOYEES.')
    print('''Your table consists of seven columns labeled ID, EMP_NAME, ADDRESS, 
          CITY, STATE, ZIP_CODE, and SALARY''')

    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()

