
import pytest
import transactions

#Completed By James Kong on 3/22/2022
@pytest.fixture
def trackerDB():
    db = "tracker.db"
    ''' create tracker database '''
    db = transactions(db)
    yield db

#Completed By James Kong on 3/22/2022
@pytest.fixture
def testShowTransactions():
    db = "tracker.db"
    transaction1 = {'item #': 3,'amount': 30, 'category': 'gaming', 'date': '03/23/22'}
    transaction2 = {'item #': 5,'amount': 20, 'category': 'pet supplies', 'date': '03/24/22'}
    transaction3 = {'item #': 2,'amount': 96, 'category': 'toiletries', 'date': '03/25/22'}
    id1= db.add(transaction1)
    id2= db.add(transaction2)
    id3= db.add(transaction3)
    yield db
    db.delete(id3)
    db.delete(id2)
    db.delete(id1)