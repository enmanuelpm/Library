import connection

from prettytable import from_db_cursor
import sqlite3

def borrowedlist(type):
    try:
        conn = connection.sql_connection()
        cur = conn.cursor()
        status = type
        cur.execute("Select id,bookid,bookname,userid,username,cdate,status,rdate from borrow where status = ?",(status,))
        records = cur.fetchall()
        print(f"{len(records)} Records found")
        if len(records) > 0:
            x = from_db_cursor(cur)
            x.field_names = ["ID","Book id","Book name","User id","User name","Date created","Status","Return Date"]
            for row in records:
                x.add_row(row)
            print(x)
        else:
            print("No records found!")
    except sqlite3.Error as e:
        print("Failed to reach the database!")
    finally:
        conn.close()

