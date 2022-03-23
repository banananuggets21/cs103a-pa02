import sqlite3

class transactions():

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
    def showTranscations(self):
        con = sqlite3.connect(self.fileName)
        cur = con.cursor()
        results = cur.execute("SELECT * FROM data")
        data = [x for x in results]
        con.commit()
        con.close()
        return data

    def addTransaction(self):
        return None

    def deleteTranscation(self):
        return None

    def sumTransactionsByDate(self):
        return None

    def sumTransactionsByMonth(self):
        return None

    def sumTransactionsByYear(self):
        return None

    def sumTransactionsByCategory(self):
        return None

