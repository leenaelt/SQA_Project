import pytest
from app.login import login

def test_invalid_password():
    assert login("admin", "wrong") == False

def test_empty_username():
    with pytest.raises(ValueError):
        login("", "1234")

def test_empty_password():
    with pytest.raises(ValueError):
        login("admin", "")
