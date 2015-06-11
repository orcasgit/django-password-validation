from password_validation import get_default_password_validators


def test_default_setting():
    """Defaults to no password validation."""
    assert get_default_password_validators() == []
