import connection
import sqlite3
import datetime
from prettytable import from_db_cursor
from borrowed import borrowedlist

def strnotnull(message):
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

def retur(id):
    try:
        conn = connection.sql_connection()
        cur = conn.cursor()
        cur.execute('''select id, bookid, bookname, userid, username, cdate, status from borrow where id = ?''',(id,))
        records = cur.fetchall()
        if len(records) > 0:
            bookid = records[0][1]

            if records[0][6] == 1:
                print(f"This borrow ID {id} is already returned!")
            else:
                table = from_db_cursor(cur)
                table.field_names = ["Borrow ID","Book id","Book name","User id","User name","Date created","Status"]
                for row in records:
                    table.add_row(row)
                print(table)
                re = strnotnull("Do you want to mark this borrow as returned? y/n: ")
                if re == "y":
                    cur.execute('''select * from book where id = ?''',(bookid,))
                    records = cur.fetchall()
                    newqty = records[0][7] + 1
                    cur.execute("update book set qty = ? where id = ?",(newqty,bookid))
                    date = datetime.date.today()
                    status = 1
                    cur.execute("update borrow set status = ? , rdate = ? where id = ?",(status,date,id))
                    conn.commit()
                    print("Record updated successfully")
                elif re == "n":
                    print("User canceled, no records updated!")
        else:
            print(f"The borrow ID {id} does not exists!")
    except sqlite3.Error as e:
        print("Database Error:!",e)
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

def returnbook():
    print("\n----Book Return----")

    text = "\n1-Return a book | 2-View borrowed list | 3-view returned list | 4-Return to main menu |\nEnter menu value number: "
    while True:
        option = inputnumber1(text)
        if option == 1:
            id = inputnumber("Borrow ID:")
            retur(id)
        elif option == 2:
            borrowedlist(0)
        elif option == 3:
            borrowedlist(1)
        elif option == 4:
            break
    return()




