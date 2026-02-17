from app.login import login

def test_valid_login():
    assert login("admin", "1234") == True
