from datetime import datetime, timedelta, timezone
from src.demo_application.app import UserSession

def test_session_not_expired():
    session = UserSession("demo_user", datetime.now(timezone.utc) - timedelta(minutes=5), 15)
    assert session.is_expired() is False

def test_session_expired():
    session = UserSession("demo_user", datetime.now(timezone.utc) - timedelta(minutes=20), 15)
    assert session.is_expired() is True
