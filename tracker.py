#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

'''
import sys
from transactions import Transaction
from category import Category

transactions = Transaction('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''




def process_choice(choice):
    ''' processes user choice '''
    if choice == '0':
        return
    elif choice == '1':
        cats = category.select_all()
        print_categories(cats)
    elif choice == '2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice == '3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid, cat)
    elif choice == '4':
        #Completed by James Kong on 3/23/2022
        trans = transactions.select_all()
        print_transactions(trans)
    elif choice == '5':
        #Completed by James Kong on 3/23/2022
        item_num = input("transaction item #: ")
        amount = input("transaction amount: ")
        trans_category = input("category: ")
        date = input("date: ")
        desc = input("description: ")
        transaction = {'item #': item_num, 'amount': amount, 'category': trans_category, 'date': date, 'description': desc}
        transactions.add_transaction(transaction)
    elif choice == '6':
        #Completed By James Kong on 3/23/2022
        delete = input("Enter transaction rowid: ")
        transactions.delete_transaction(delete)
    elif choice=='7':
        #Completed By Jeremy Bernstein on 3/23/2022
        trans = transactions.select_all()
        transactions.sum_transactions_by_date()
    elif choice=='8':
        #Completed by Jeremy Bernstein on 3/23/2022
        trans = transactions.select_all()
        transactions.sum_transactions_by_month()
    elif choice=='9':
        #Completed by Jeremy Bernstein on 3/23/2022
        trans = transactions.select_all()
        transactions.sum_transactions_by_year()
    elif choice == '10':
        #Complated by Hiro Chen on 3/25/2022
        trans = transactions.select_all()
        transactions.sum_transactions_by_category()
    elif choice == '11':
        #Completed by James Kong on 3/21/2022
        print(menu)
    else:
        print("choice", choice, "not yet implemented")

    choice = input("> ")
    return(choice)


def toplevel():
    ''' handle the user's choice read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice != '0':
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items) == 0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s" % ('item #', 'amount', 'category', 'date', 'description'))
    print('-'*40)
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10s %-10s %-10s %-30s" % values)

def print_category(cat):
    ''' prints category '''
    print("%-3d %-10s %-30s" % (cat['rowid'], cat['name'], cat['desc']))

def print_categories(cats):
    ''' prints categories '''
    print("%-3s %-10s %-30s" % ("id", "name", "description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)

# here is the main call!

toplevel()
