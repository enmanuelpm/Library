import connection
import sqlite3
import textwrap
from prettytable import from_db_cursor
#from playhouse.sqlite_ext import SqliteExtDatabase

def search_func(text):
    try:
        conn = connection.sql_connection()
        cur = conn.cursor()
        cur.execute('''select rowid, name, author, isbn, publisher from book_index
                    where book_index match ?;''',(text,))
                    # id like ? or name like ? or desc like ? or author like ? or isbn like ?
                    #or publisher like ?''',('%'+text+'%','%'+text+'%','%'+text+'%','%'+text+'%','%'+text+'%','%'+text+'%'))
        records = cur.fetchall()
        if len(records) > 0:
            print(f"\n{len(records)} Results found.") #print how many results found
            table = from_db_cursor(cur) #new table from the prettytable class
            table.field_names = ["ID","Name","Author","ISBN","Publisher"] #Table headers
            for row in records:
                table.add_row(row) #add rows to table from database cursor
            print(table) #print table
        else:
            print("Search did not return any results.")

    except sqlite3.Error as e:
        print("Database error: !",e)
    finally:
        conn.close()

def allbooklist():
    try:
        conn = connection.sql_connection()
        cur = conn.cursor()
        cur.execute('''select id, name , author, isbn, edition, publisher, location, qty from book''')
        records = cur.fetchall()
        if len(records) > 0:
            print(f"\n{len(records)} Results found.") #print how many results found
            table = from_db_cursor(cur) #new table from the prettytable class
            table.field_names = ["ID","Name","Author","ISBN","Edition","Publisher","Location","Qty."] #Table headers
            for row in records:
                table.add_row(row) #add rows to table from database cursor
            print(table) #print table
        else:
            print("Search did not return any results.")
    except sqlite3.Error as e:
        print("Database error: !",e)
    finally:
        conn.close()

def format1(text1,text2): #function to format the list view
    print('\033[1m'+text1.rjust(9) + ':\t' + '\033[0m' + str(text2) )
    return

def book_detail(id): #function to print book in detail view
    try:
        conn = connection.sql_connection()
        cur = conn.cursor()
        cur.execute('''select id, name, desc, author, isbn, edition, publisher, location, qty  from book where id = ?;''',(id,))
        records = cur.fetchall()
        dash = "-" * 90
        if len(records) > 0:
            print(dash)
            format1('Book ID',records[0][0])
            format1('Name',records[0][1])
            format1('Author',records[0][3])
            format1('ISBN',records[0][4])
            format1('Edition',records[0][5])
            format1('Publisher',records[0][6])
            format1('Location',records[0][7])
            format1('Qty',records[0][1])
            wrapper = textwrap.TextWrapper(width=80)
            if records[0][2] != None:
                print("\033[1mDescription: \033[0m ")
                desc = wrapper.wrap(text=records[0][2])
                for line in desc:
                    print(line)

            else:
                print("\033[1mDescription: \033[0m None")
            print(dash)
        else:
            print("The book ID: [" + str(id) + "] does not exists:")

    except sqlite3.Error as e:
        print("Database error: !",e)
    finally:
        conn.close()

def inputnumber1(message):
    while True:
        try:
            n = int(input(message))
            if n == 1 or n == 2 or n == 3 or n == 4:
                break
            else:
                print("Not a valid option try again!")
        except ValueError:
            print('Not a valid input! "Integer expected" try again')
            continue
    return n

def inputnumber(message):
    while True:
        try:
            n = int(input(message))
            if n <= 0:
                print("Not negative value allowed try again!")
            else:
                break
        except ValueError:
            print('Not a valid input! "Integer expected" try again')
            continue
    return n

def search():
    print("\n----Search Book----")

    text = "\n1-New search | 2-View book details | 3-View all book list | 4-Return to main menu |\nEnter menu value number: "
    while True:
        option = inputnumber1(text)
        if option == 4:
            break
        elif option == 1:
            sc = str(input("Search text: ")).strip().lower()
            search_func(sc)
        elif option == 2:
            book_detail(inputnumber('\nBook ID:'))
        elif option == 3:
            allbooklist()

    return


