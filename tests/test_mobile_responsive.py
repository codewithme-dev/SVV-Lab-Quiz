from src.demo_application.app import is_mobile_layout_supported

def test_mobile_viewport_supported():
    assert is_mobile_layout_supported(375) is True

def test_desktop_viewport_not_mobile():
    assert is_mobile_layout_supported(1440) is False
