from src.demo_application.app import authenticate_user

def test_valid_login():
    assert authenticate_user("demo_user", "Demo@12345") is True

def test_invalid_login():
    assert authenticate_user("demo_user", "wrong") is False
