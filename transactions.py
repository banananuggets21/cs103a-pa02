import sqlite3

def to_trans_dict(trans_tuple):
    '''Completed By James Kong on 3/23/2022'''
    trans = {'item #':trans_tuple[1], 'amount':trans_tuple[2], 'category':trans_tuple[3], 'date':trans_tuple[4], 'description':trans_tuple[5]}
    return trans

def to_trans_dict_list(trans_tuples):
    '''Completed By James Kong on 3/23/2022'''
    return [to_trans_dict(tran) for tran in trans_tuples]

class Transaction():

    def __init__(self, file_name):
        '''Completed By James Kong on 3/23/2022'''
        con = sqlite3.connect(file_name)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions ('item num' int, amount int, category text, date int, description text)''')
        con.commit()
        con.close()
        self.file_name = file_name

    def select_all(self):
        '''Completed By James Kong on 3/23/2022'''
        con = sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    def select_one(self, rowid):
        '''Completed By James Kong on 3/23/2022'''
        con = sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute("SELECT rowid, * from transactions where rowid = (?)", (rowid,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict(tuples[0])

    def add_transaction(self, item):
        '''Completed By James Kong on 3/23/2022'''
        con = sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)", (item['item #'], item['amount'], item['category'], item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def delete_transaction(self, rowid):
        '''Completed By James Kong on 3/23/2022'''
        con = sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions WHERE rowid = (?); ''', (rowid,))
        con.commit()
        con.close()

    #Completed by Jeremy Bernstein on 3/23/2022
    def sum_transactions_by_date(self):
        con= sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute("SELECT date,* FROM transactions group by date")
        date = ([row[0] for row in cur.fetchall()])
        for month in date:
            monthStr = str(month)
            print(monthStr[4:6] + "-" + monthStr[6:8] + "-" + monthStr[0:4])
        con.commit()
        con.close()
        return None

    #Completed by Jeremy Bernstein on 3/23/2022
    def sum_transactions_by_month(self):
        con= sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute("SELECT date, * from transactions group by date")
        date = (row[0] for row in cur.fetchall())
        for month in date:
            monthstr = str(month)
            print(monthstr[4:6])
        con.commit()
        con.close()
        return None

    #Completed by Jeremy Bernstein on 3/23/2022
    def sum_transactions_by_year(self):
        con= sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute("SELECT date, * from transactions group by date")
        date = (row[0] for row in cur.fetchall())
        for month in date:
            monthStr = str(month)
            print(monthStr[0:4])
        con.commit()
        con.close()
        return None

    #Completed by Hiro Chen on 3/24/2022
    def sum_transactions_by_category(self):
        con = sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute("SELECT category from transactions")
        #Need help with finding the correct position of category
        category = (row[0] for row in cur.fetchall())
        con.commit()
        con.close()
        return category
