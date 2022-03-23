import sqlite3

#Completed By James Kong on 3/23/2022
def to_trans_dict(trans_tuple):
    trans = {'rowid':trans_tuple[0], 'item #':trans_tuple[1], 'amount':trans_tuple[2], 'category':trans_tuple[3], 'date':trans_tuple[4], 'description':trans_tuple[5]}
    return trans

#Completed By James Kong on 3/23/2022
def to_trans_dict_list(trans_tuples):
    return [to_trans_dict(tran) for tran in trans_tuples]

class Transaction():

    #Completed By James Kong on 3/23/2022
    def __init__(self, fileName):
        self.fileName = fileName
        con = sqlite3.connect(fileName)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions 
        ('item num' int, amount int, category text, date text, description text)''')
        con.commit()
        con.close()
        self.fileName = fileName

    #Completed By James Kong on 3/23/2022
    def select_all(self):
        con= sqlite3.connect(self.fileName)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    #Completed By James Kong on 3/23/2022
    def select_one(self,rowid):
        ''' return a category with a specified rowid '''
        con= sqlite3.connect(self.fileName)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict(tuples[0])
    
    #Completed By James Kong on 3/23/2022
    def addTransaction(self, item):
        con= sqlite3.connect(self.fileName)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item #'],item['amount'], item['category'], item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    #Completed By James Kong on 3/23/2022
    def deleteTransaction(self, rowid):
        con= sqlite3.connect(self.fileName)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()

    def sumTransactionsByDate(self):
        return None

    def sumTransactionsByMonth(self):
        return None

    def sumTransactionsByYear(self):
        return None

    def sumTransactionsByCategory(self):
        return None

