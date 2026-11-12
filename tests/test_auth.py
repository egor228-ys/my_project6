import pytest
from src.auth.auth_service import AuthService
from src.auth.exceptions import ValidationError, UserExistsError, InvalidCredentialsError

def test_register_success():
    auth = AuthService()
    assert auth.register("ivan", "123456") is True

def test_register_empty_username():
    auth = AuthService()
    with pytest.raises(ValidationError):
        auth.register("", "123456")

def test_register_short_password():
    auth = AuthService()
    with pytest.raises(ValidationError):
        auth.register("ivan", "123")

def test_register_existing_user():
    auth = AuthService()
    auth.register("ivan", "123456")
    with pytest.raises(UserExistsError):
        auth.register("ivan", "654321")

def test_login_success():
    auth = AuthService()
    auth.register("ivan", "123456")
    assert auth.login("ivan", "123456") is True

def test_login_wrong_password():
    auth = AuthService()
    auth.register("ivan", "123456")
    with pytest.raises(InvalidCredentialsError):
        auth.login("ivan", "wrong")

def test_login_empty_password():
    auth = AuthService()
    with pytest.raises(ValidationError):
        auth.login("ivan", "")
