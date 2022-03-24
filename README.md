Brandeis University: COSI 103A - Fundamentals of Software Engineering

This repository was created for class projects/assignments. It will primarily house the file contents of the PA02 assignment, which contains a dataset of Brandeis course selections, professors, and etc.

Team Members: James Kong, Jeremy Bernstein, Hiro Chen

```
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
```