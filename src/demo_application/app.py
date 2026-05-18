"""Demo application helper functions for validation tests."""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass
class UserSession:
    username: str
    last_activity: datetime
    timeout_minutes: int = 15

    def is_expired(self, now: datetime | None = None) -> bool:
        now = now or datetime.now(timezone.utc)
        return now - self.last_activity > timedelta(minutes=self.timeout_minutes)


def authenticate_user(username: str, password: str) -> bool:
    return username == "demo_user" and password == "Demo@12345"


def calculate_transfer(source_balance: float, destination_balance: float, amount: float) -> tuple[float, float]:
    if amount <= 0:
        raise ValueError("Transfer amount must be greater than zero")
    if amount > source_balance:
        raise ValueError("Insufficient balance")
    return round(source_balance - amount, 2), round(destination_balance + amount, 2)


def is_mobile_layout_supported(viewport_width: int) -> bool:
    return viewport_width <= 768


def log_event(event_type: str, username: str) -> dict[str, str]:
    return {
        "event_type": event_type,
        "username": username,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
