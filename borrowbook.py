import connection
import datetime
import sqlite3

# def validate(message): #function to validate the date
#     while True:
#         date_i = str(input(message)).strip()
#         r=datetime.datetime.strptime("2000-01-01", '%Y-%m%d')
#         if date_i == "0":
#
#         else:
#             try:
#                 date_d=datetime.datetime.strptime(date_i, '%m-%d-%Y').date()
#                 #print(date_d)
#             except ValueError:
#                 print("Incorrect data format, should be MM-DD-YYYY")
#             if date_d < datetime.date.today():
#                 print("this date is in the past please try again!")
#                 continue
#             else:
#                 break
#     return date_d

def inputnumber(message):
    while True:
        try:
            n = int(input(message))
            if n < 0:
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
            v = str(input(message)).strip().lower()
            if v == 'y' or v == 'n':
                break
            else:
                print(f"{v} is not a valid option please try again!")
                continue
        except ValueError:
            print("Value error!")
    return v
def verifybook(id):
    conn = connection.sql_connection()
    cur = conn.cursor()
    cur.execute('''select * from book where id = ?''',(id,))
    records = cur.fetchall()
    r = ""
    if len(records) == 0:
        print(f"The book with the ID:{id} does not exist please try again or enter 0 to cancel!")
    elif records[0][7] > 0:
        r = records[0][1]
    else:
        print(f"Te book {id} {records[0][1]} is not available!")
    cur.close()
    conn.close()
    return r
def verifyuser(id):
    conn = connection.sql_connection()
    cur = conn.cursor()
    cur.execute('''select * from users where id = ?''',(id,))
    records = cur.fetchall()
    r = ""
    if len(records) == 0:
        print(f"The user with the ID:{id} does not exist please try again or enter 0 to cancel!")
    else:
        r = records[0][1]
    cur.close()
    conn.close()
    return r

def borrowbook(): #function to borrow a book.
    while True: # While true keep asking for a valid book id number
        bookid = inputnumber("Book ID or 0 to cancel: ") #call function to input number
        if bookid == 0: # if the bookid is 0 the user canceled
            print("User Canceled, no records saved!")
            return #return to main manu
        else:
            bookname = verifybook(bookid) # if the value is not cero search in database.
            if bookname == "": # If the return is none the book doesn't exist
                continue #continue asking for a valid number
            else:
                break #else break the while and continue
    print(f"\tBook name: {bookname}") # Print the book name
    while True: # While true keep asking for a valid user id number
        userid = inputnumber("User ID or 0 to cancel: ") #call function to input number
        if userid == 0: # if the userid is 0 the user canceled
            print("User Canceled, no records saved!")
            return #return to main manu
        else:
            username = verifyuser(userid) # if the value is not cero search in database.
            if username == "": # If the return is none the user doesn't exist
                continue #continue asking for a valid number
            else:
                break #else break the while and continue
    print(f"\tNombre usuario: {username}") # print the user name
    cdate = datetime.date.today()
    status = 0
    save = strnotnull("Do you want to save? y/n: ")

    if save == 'y':
        try:
            conn = connection.sql_connection()
            cur = conn.cursor()
            cur.execute('''select * from book where id = ?''',(bookid,))
            records = cur.fetchall()
            newqty = records[0][7] - 1
            cur.execute("update book set qty = ? where id = ?",(newqty,bookid))
            conn.execute("INSERT INTO borrow (bookid,bookname,userid,username,cdate,status) VALUES (?,?,?,?,?,?)",(bookid,bookname,userid,username,cdate,status))
            conn.commit()
            print(''"\nrecord created successfully\n"'')
        except sqlite3.Error as e:
            print("Failed to create new borrow",e)
        finally:
            conn.close()
    else:
        print("User cancelled, record not saved!")
        return
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

def borrow():
    print("\n----Borrow a book----")
    text = "\n1-borrow a book | 2-Return to main menu |\nEnter menu value number: "
    while True:
        option = inputnumber1(text)
        if option == 1:
            borrowbook()
        elif option == 2:
            break
    return
