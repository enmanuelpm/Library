from newbook import newbook
from borrowbook import borrow
import os
from connection import createtables
from borrowed import borrowedlist
from search import search
from search import allbooklist
from returnbook import returnbook
from user import user
os.system('cls')
createtables()

print("\n\033[1m-----------Welcome to the Library Managment System---------------")

menu_n = 7
while True:

    print("\n| 1-New Book | 2-Borrow a Book | 3-Search Book | 4-Borrowed List | 5-Books List | 6-Return a Book | 7-Users | 8-Exit |\033[0m\n")
    try:
        o =int(input("Enter the menu option number:"))
        #print("valor seleccionado: " + str(o))
        if o == 1:
            os.system('cls')
            newbook()
            os.system('cls')
        elif o == 2:
            os.system('cls')
            borrow()
            os.system('cls')
        elif o == 3:
            os.system('cls')
            search()
            os.system('cls')
        elif o == 4:
            os.system('cls')
            borrowedlist(0)
        elif o == 5:
            os.system('cls')
            allbooklist()

        elif o == 6:
            os.system('cls')
            returnbook()
            os.system('cls')
        elif o == 7:
            os.system('cls')
            user()
            os.system('cls')
        elif o == 8:
            break
        else:
            print("\nEnter a value between 1 and 8!\n")
        #os.system('cls')
    except ValueError:
        print("\nNot a valid option enter a valid number!\n")

