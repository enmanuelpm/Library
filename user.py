import connection
import sqlite3
from prettytable import from_db_cursor
def strnotnull(message):
    while True:
        try:
            v = str(input(message)).strip()
            if v == '':
                print("Not null allowed! please enter value.")
            else:
                break
        except ValueError:
            print("Value error!")
    return v

def answer(message):
    while True:
        try:
            v = str(input(message)).strip().lower()
            if v == 'y' or v == 'n':
                break
            else:
                print(f"{v} is not a valid option please try again!")
                continue
        except ValueError:
            print("Value error!")
    return v

def addnewuser():
    print("----Create new user-----")
    name = strnotnull("Name: ")
    address = strnotnull("Address: ")
    phone = strnotnull("Phone #: ")
    r = answer("Do you want to create the new user? y/n: ")
    if r == "y":
        conn = connection.sql_connection()
        try:
            conn.execute("INSERT INTO users (NAME,address,phone) VALUES (?,?,?)",(name,address,phone))
            conn.commit()
            print(''"\nUser created successfully\n"'')

        except sqlite3.Error as e:
            print("Failed to create new user",e)
        finally:
            conn.close()
    else:
        print("User canceled, User not created!")

def viewusers():
    conn = connection.sql_connection()
    try:
        cur = conn.cursor()
        cur.execute("select * from users")
        records = cur.fetchall()
        print(f"{len(records)} Records found")
        if len(records) > 0:
            table = from_db_cursor(cur)
            table.field_names = ["ID","Name","Address","Phone"]
            for row in records:
                table.add_row(row)
            print(table)
        else:
            print("No records found!")
    except sqlite3.Error as e:
        print("Database error!",e)
    finally:
        conn.close()

def inputnumber1(message):
    while True:
        try:
            n = int(input(message))
            if n == 1 or n == 2 or n == 3:
                break
            else:
                print("Not a valid option try again!")
        except ValueError:
            print('Not a valid input! "Integer expected" try again')
            continue
    return n

def user():
    print("----Users----")
    text = "\n| 1-Create new user | 2-View all users | 3-Return to main menu |\nEnter menu value number: "
    while True:
        option = inputnumber1(text)
        if option == 1:
            addnewuser()
        elif option == 2:
            viewusers()
        elif option == 3:
            break
    return
