Brandeis University: COSI 103A - Fundamentals of Software Engineering

This repository was created for class projects/assignments. It will primarily house the file contents of the PA02 assignment, which contains a dataset of Brandeis course selections, professors, and etc.

Team Members: James Kong, Jeremy Bernstein, Hiro Chen

```
jameskong@Jimmy-Ks-Laptop:/mnt/c/users/james/onedrive/desktop/Personal GitHub Repos/cs103a/cs103a-pa02$ pytest -v test_transactions.py
================================================= test session starts =================================================
platform win32 -- Python 3.9.7, pytest-7.1.1, pluggy-0.12.0 -- C:\Users\james\miniconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\james\onedrive\desktop\Personal GitHub Repos\cs103a\cs103a-pa02, configfile: pytest.ini
collected 6 items

test_transactions.py::test_addTransactions PASSED                                                                [ 16%]
test_transactions.py::test_delete PASSED                                                                         [ 33%]
test_transactions.py::test_date FAILED                                                                           [ 50%]
test_transactions.py::test_month FAILED                                                                          [ 66%]
test_transactions.py::test_year FAILED                                                                           [ 83%]
test_transactions.py::test_category FAILED                                                                       [100%]

====================================================== FAILURES =======================================================
______________________________________________________ test_date ______________________________________________________

small_DB = <transactions.Transaction object at 0x000001E73DF53C10>

    @pytest.mark.date
    def test_date(small_DB):
        transactions0 = small_DB.select_all()
        transaction0 = {'item #': 5,'amount': 10, 'category': 'fruit', 'date': '20220323', 'description': 'banana'}
        #rowid = small_DB.add_transaction(transaction0)
>       assert small_DB.sum_transactions_by_date() == '20220323'
E       AssertionError: assert <generator object Transaction.sum_transactions_by_date.<locals>.<genexpr> at 0x000001E73DF873C0> == '20220323'
E        +  where <generator object Transaction.sum_transactions_by_date.<locals>.<genexpr> at 0x000001E73DF873C0> = <bound method Transaction.sum_transactions_by_date of <transactions.Transaction object at 0x000001E73DF53C10>>()
E        +    where <bound method Transaction.sum_transactions_by_date of <transactions.Transaction object at 0x000001E73DF53C10>> = <transactions.Transaction object at 0x000001E73DF53C10>.sum_transactions_by_date

test_transactions.py:61: AssertionError
_____________________________________________________ test_month ______________________________________________________

small_DB = <transactions.Transaction object at 0x000001E73DF9A700>

    @pytest.mark.month
    def test_month(small_DB):
        transactions0 = small_DB.select_all()
        transaction0 = {'item #': 5,'amount': 10, 'category': 'fruit', 'date': '20220323', 'description': 'banana'}
        #rowid = small_DB.add_transaction(transaction0)
>       assert small_DB.sum_transactions_by_month() == '03'

test_transactions.py:69:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
transactions.py:80: in sum_transactions_by_month
    for month in date:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

.0 = <list_iterator object at 0x000001E73DF9AA60>

>   date = (row[2] for row in cur.fetchall())
E   IndexError: tuple index out of range

transactions.py:79: IndexError
______________________________________________________ test_year ______________________________________________________

small_DB = <transactions.Transaction object at 0x000001E73DF83910>

    @pytest.mark.year
    def test_year(small_DB):
        transactions0 = small_DB.select_all()
        transaction0 = {'item #': 5,'amount': 10, 'category': 'fruit', 'date': '20220323', 'description': 'banana'}
        #rowid = small_DB.add_transaction(transaction0)
>       assert small_DB.sum_transactions_by_year() == '2022'

test_transactions.py:77:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
transactions.py:92: in sum_transactions_by_year
    for year in date:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

.0 = <list_iterator object at 0x000001E73DF839D0>

>   date = (row[2] for row in cur.fetchall())
E   IndexError: tuple index out of range

transactions.py:91: IndexError
____________________________________________________ test_category ____________________________________________________

small_DB = <transactions.Transaction object at 0x000001E73DF520A0>

    @pytest.mark.year
    def test_category(small_DB):
        transactions0 = small_DB.select_all()
        transaction0 = {'item #': 5,'amount': 10, 'category': 'fruit', 'date': '20220323', 'description': 'banana'}
>       assert small_DB.sum_transactions_by_category() == 'fruit'

test_transactions.py:84:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <transactions.Transaction object at 0x000001E73DF520A0>

    def sum_transactions_by_category(self):
        con = sqlite3.connect(self.file_name)
        cur = con.cursor()
>       cur.exceute("SELECT date from transactions")
E       AttributeError: 'sqlite3.Cursor' object has no attribute 'exceute'

transactions.py:102: AttributeError
=============================================== short test summary info ===============================================
FAILED test_transactions.py::test_date - AssertionError: assert <generator object Transaction.sum_transactions_by_dat...
FAILED test_transactions.py::test_month - IndexError: tuple index out of range
FAILED test_transactions.py::test_year - IndexError: tuple index out of range
FAILED test_transactions.py::test_category - AttributeError: 'sqlite3.Cursor' object has no attribute 'exceute'
============================================= 4 failed, 2 passed in 0.44s =============================================

jameskong@Jimmy-Ks-Laptop:/mnt/c/users/james/onedrive/desktop/Personal GitHub Repos/cs103a/cs103a-pa02$ pylint transactions.py
************* Module transactions
transactions.py:5:0: C0301: Line too long (166/100) (line-too-long)
transactions.py:18:0: C0301: Line too long (138/100) (line-too-long)
transactions.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:47:0: C0301: Line too long (152/100) (line-too-long)
transactions.py:62:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:65:11: C0326: Exactly one space required before assignment
        con= sqlite3.connect(self.file_name)
           ^ (bad-whitespace)
transactions.py:76:11: C0326: Exactly one space required before assignment
        con= sqlite3.connect(self.file_name)
           ^ (bad-whitespace)
transactions.py:85:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:88:11: C0326: Exactly one space required before assignment
        con= sqlite3.connect(self.file_name)
           ^ (bad-whitespace)
transactions.py:99:0: C0304: Final newline missing (missing-final-newline)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:12:0: C0115: Missing class docstring (missing-class-docstring)
transactions.py:64:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:87:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:98:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:98:4: R0201: Method could be a function (no-self-use)

------------------------------------------------------------------
Your code has been rated at 7.76/10 (previous run: 5.39/10, +2.37)

jameskong@Jimmy-Ks-Laptop:/mnt/c/users/james/onedrive/desktop/Personal GitHub Repos/cs103a/cs103a-pa02$ pylint tracker.py
************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:80:23: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:91:0: C0301: Line too long (123/100) (line-too-long)
tracker.py:97:15: C0326: Exactly one space required around comparison
    elif choice=='7':
               ^^ (bad-whitespace)
tracker.py:101:15: C0326: Exactly one space required around comparison
    elif choice=='8':
               ^^ (bad-whitespace)
tracker.py:105:15: C0326: Exactly one space required around comparison
    elif choice=='9':
               ^^ (bad-whitespace)
tracker.py:116:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:140:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:157:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:37:0: C0103: Constant name "transactions" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:38:0: C0103: Constant name "category" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:43:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:63:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:61:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:137:10: E1307: Argument 'builtins.str' does not match format type 'd' (bad-string-format-type)
tracker.py:137:10: E1307: Argument 'builtins.str' does not match format type 'd' (bad-string-format-type)
tracker.py:33:0: W0611: Unused import sys (unused-import)

------------------------------------------------------------------
Your code has been rated at 6.71/10 (previous run: 6.54/10, +0.17)

jameskong@Jimmy-Ks-Laptop:/mnt/c/users/james/onedrive/desktop/Personal GitHub Repos/cs103a/cs103a-pa02$ python3 tracker.py

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

> 5
transaction item #: 1
transaction amount: 3
category: food
date: 20220312
description: banana
> 5
transaction item #: 2
transaction amount: 3200
category: food
date: 20220512
description: apple
> 5
transaction item #: 3
transaction amount: 123201
category: food
date: 20220512
description: pear
> 4


item #     amount     category   date       description
----------------------------------------
1          3          food       20220312   banana
2          3200       food       20220512   apple
3          123201     food       20220512   pear
> 6
Enter transaction rowid: 2
> 4


item #     amount     category   date       description
----------------------------------------
1          3          food       20220312   banana
3          123201     food       20220512   pear
>
```