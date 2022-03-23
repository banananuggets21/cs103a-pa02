
import pytest
from transactions import Transaction

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

#Completed By James Kong on 3/23/2022
@pytest.fixture
def small_DB(empty_db):
    transaction1 = {'item #': 3,'amount': 30, 'category': 'gaming', 'date': '03/23/22', 'description': '144hz monitor'}
    transaction2 = {'item #': 5,'amount': 20, 'category': 'pet supplies', 'date': '03/24/22', 'description': 'litter box'}
    id1= empty_db.add(transaction1)
    id2= empty_db.add(transaction2)
    yield empty_db
    empty_db.delete(id2)
    empty_db.delete(id1)

#Completed By James Kong on 3/23/2022
@pytest.mark.add
def test_addTransactions(small_DB):
    testTransaction = {'item #': 2,'amount': 96, 'category': 'toiletries', 'date': '03/25/22', 'description': 'toilet paper'}
    transactions0 = small_DB.showTransactions()
    rowid = small_DB.add(testTransaction)
    transactions1 = small_DB.select_all()
    assert len(transactions1) == len(transactions0) + 1
    transaction1 = small_DB.select_one(rowid)
    assert transaction1['item #']==testTransaction['item #']
    assert transaction1['amount']==testTransaction['amount']
    assert transaction1['category']==testTransaction['category']
    assert transaction1['date']==testTransaction['date']

#Completed By James Kong on 3/23/2022
@pytest.mark.delete
def test_delete(small_DB):
    transactions0 = small_DB.select_all()
    transaction0 = {'item #': 5,'amount': 10, 'category': 'fruit', 'date': '05/10/22', 'description': 'banana'}
    rowid = small_DB.add(transaction0)
    transactions1 = small_DB.select_all()
    small_DB.delete(rowid)
    transactions2 = small_DB.select_all()
    assert len(transactions0)==len(transactions2)
    assert len(transactions2) == len(transactions1)-1