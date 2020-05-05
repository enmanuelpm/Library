import connection
import sqlite3
def inputnumber(message):
    while True:
        try:
            n = int(input(message))
            if n <= 0:
                print("Not negative value allowed")
            else:
                break
        except ValueError:
            print('Not a valid input! "Integer expected" try again')
            continue
    return n

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
# def editbook():
#     print("--Edit book--")
#     while True:
#         id = inputnumber("Enter book ID to edit: ")
#         conn = connection.sql_connection()
#         cur = conn.cursor()
#         cur.excecute("select * from book where ")

def addnewbook():
    print("\n---New Book Entry---\n")
    name = strnotnull("Name: ")
    desc = strnotnull("Description: ")
    author = strnotnull("Author: ")
    isbn = strnotnull("ISBN: ")
    edition = inputnumber("Edition: ")
    publisher = strnotnull("Publisher: ")
    location = strnotnull("Location: ")
    qty = inputnumber("Quantity: ")
    r = answer("Save the new book? y/n: ")
    if r == "y":
        conn = connection.sql_connection()
        try:
            conn.execute("INSERT INTO book (NAME,desc,author,isbn,edition,publisher,location,qty) VALUES (?,?,?,?,?,?,?,?)",(name,desc,author,isbn,edition,publisher,location,qty))
            conn.commit()
            print(''"\nrecord created successfully\n"'')

        except sqlite3.Error as e:
            print("Failed to create new book",e)
        finally:
            conn.close()
    else:
        print("User canceled, book not saved!")

def inputnumber1(message):
    while True:
        try:
            n = int(input(message))
            if n == 1 or n == 2:
                break
            else:
                print("Not a valid option try again!")
        except ValueError:
            print('Not a valid input! "Integer expected" try again')
            continue
    return n

def newbook():
    print("\n----New Book----")
    text = "\n1-New Book | 2-Return to main menu |\nEnter menu value number: "
    while True:
        option = inputnumber1(text)
        if option == 1:
            addnewbook()
        elif option == 2:
            break
    return

