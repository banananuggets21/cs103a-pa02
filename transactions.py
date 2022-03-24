import sqlite3

def to_trans_dict(trans_tuple):
    '''Completed By James Kong on 3/23/2022'''
    trans = {'rowid':trans_tuple[0], 'item #':trans_tuple[1], 'amount':trans_tuple[2], 'category':trans_tuple[3], 'date':trans_tuple[4], 'description':trans_tuple[5]}
    return trans

def to_trans_dict_list(trans_tuples):
    '''Completed By James Kong on 3/23/2022'''
    return [to_trans_dict(tran) for tran in trans_tuples]

class Transaction():

    def __init__(self, file_name):
        '''Completed By James Kong on 3/23/2022'''
        con = sqlite3.connect(file_name)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions ('item num' int, amount int, category text, date text, description text)''')
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
    
    def sum_transactions_by_date(self):
        return None

    def sum_transactions_by_month(self):
        return None

    def sum_transactions_by_year(self):
        return None

    def sum_transactions_by_category(self):
        return None