
import pytest
import transactions

#Completed By James Kong on 3/22/2022
@pytest.fixture
def trackerDB():
    db = "tracker.db"
    ''' create tracker database '''
    db = transactions(db)
    yield db