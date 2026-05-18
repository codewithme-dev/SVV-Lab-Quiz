import pytest
from src.demo_application.app import calculate_transfer

def test_transfer_accuracy():
    new_source, new_destination = calculate_transfer(1000.0, 500.0, 250.0)
    assert new_source == 750.0
    assert new_destination == 750.0

def test_transfer_rejects_negative_amount():
    with pytest.raises(ValueError):
        calculate_transfer(1000.0, 500.0, -10.0)
