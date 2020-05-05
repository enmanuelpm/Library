import sqlite3
from sqlite3 import Error

def sql_connection(): #this function create a connection to the database if it doesn't exist it is created.
        try:
            conn = sqlite3.connect('library.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
            #print("Open database successfuly")
            return conn
        except Error:
            print(Error)
            print('exiting system..."')
            exit()



def createtables():
    conn = sql_connection()
    cursorObj = conn.cursor()
    try:
        cursorObj.execute('''create table if not exists USERS(
                                ID integer primary key autoincrement not null,
                                NAME text not null,
                                ADDRESS char(50),
                                PHONE char(20))''')

        cursorObj.execute('''create table if not exists book(
                                ID integer primary key autoincrement not null,
                                NAME text not null,
                                desc text,
                                author text not null,
                                isbn char(20) not null,
                                edition int, publisher text,
                                location char(15),
                                qty int not null)''')

        cursorObj.execute('''create table if not exists borrow(
                                ID integer primary key autoincrement not null,
                                bookid integer not null,
                                bookname text not null,
                                userid integer not null,
                                username text not null,
                                cdate date not null,
                                status boolean not null,
                                rdate date)''')
        cursorObj.execute('''CREATE VIRTUAL TABLE if not exists book_index USING fts5(name, desc, author, isbn, publisher)''')
        cursorObj.execute('''CREATE TRIGGER if not exists after_book_insert AFTER INSERT ON book BEGIN
                                INSERT INTO book_index (rowid, name, desc, author, isbn, publisher)
                                VALUES(new.id, new.name, new.desc, new.author, new.isbn, new.publisher); END;''')
        cursorObj.execute('''create trigger if not exists after_book_update after update on book 
        BEGIN UPDATE book_index SET name = new.name, desc = new.desc, author = new.author, 
        isbn = new.isbn, publisher = new.publisher WHERE rowid = old.id; END;''')

        cursorObj.execute('''create trigger if not exists after_book_delete after delete on book 
                            begin delete from book_index where rowid = old.id; end;''')
        conn.commit()
        print("Tables created successfully")
    except sqlite3.Error as e:
        print("Failed to create databases: ",e)
        exit()
    finally:
        cursorObj.close() #close the cursor
        conn.close()

    # name = "Jose Herrera"
    # address = "25 Main st."
    # phone = "978-875-78954"
    # conn.execute("INSERT INTO USERS (NAME,ADDRESS,PHONE) VALUES (?,?,?)",(name,address,phone))
    # conn.commit()
    # cursor = conn.execute("select * from USERS") #Select all the records in the USERS table.
    # dash = "-" * 70
    # print(dash)
    # print('{:<6}{:<20}{:<30}{:<18}'.format("ID","Name","Address","Phone",)) # print the table headers
    # print(dash)
    # for row in cursor:
    #     print('{:<6}{:<20}{:<30}{:<18}'.format(row[0],row[1],row[2],row[3])) # Print all the records from the table.
