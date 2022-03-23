import sqlite3

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
    def selectAll(self):
        con = sqlite3.connect(self.fileName)
        cur = con.cursor()
        results = cur.execute("SELECT * FROM data")
        data = [x for x in results]
        con.commit()
        con.close()
        return data
    
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
        cur.execute('''DELETE FROM categories
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

