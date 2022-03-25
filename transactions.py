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
        cur.execute("SELECT date from transactions")
        date = (row[2] for row in cur.fetchall())
        #date = date[1:]
        con.commit()
        con.close()
        return date

    #Completed by Jeremy Bernstein on 3/23/2022
    def sum_transactions_by_month(self):
        con= sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute("SELECT date from transactions")
        date = (row[2] for row in cur.fetchall())
        for month in date:
            month = month[4:5]
        con.commit()
        con.close()
        return date
    
    #Completed by Jeremy Bernstein on 3/23/2022
    def sum_transactions_by_year(self):
        con= sqlite3.connect(self.file_name)
        cur = con.cursor()
        cur.execute("SELECT date from transactions")
        date = (row[2] for row in cur.fetchall())
        for year in date:
            year = year[0:3]
        con.commit()
        con.close()
        return date

    def sum_transactions_by_category(self):
        return None