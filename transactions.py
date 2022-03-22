import sqlite3

class transactions():

    def __init__(self, fileName):
        self.fileName = fileName
        con = sqlite3.connect(fileName)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions 
        ('item num' int, 'amount' int, 'category' text, 'date' text, 'description' text)''')

    def showTranscations():
        return None

    def addTransaction():
        return None

    def deleteTranscation():
        return None

    def sumTransactionsByDate():
        return None

    def sumTransactionsByMonth():
        return None

    def sumTransactionsByYear():
        return None

    def sumTransactionsByCategory():
        return None

