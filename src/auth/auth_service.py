import logging
from .exceptions import ValidationError, UserExistsError, InvalidCredentialsError

logger = logging.getLogger(__name__)

class AuthService:
    def __init__(self):
        self.users = {}

    def register(self, username: str, password: str) -> bool:
        if not username or not password:
            raise ValidationError("Username and password cannot be empty")
        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters")
        if username in self.users:
            logger.warning(f"Attempt to register existing user: {username}")
            raise UserExistsError(f"User {username} already exists")
        self.users[username] = password
        logger.info(f"Registered new user: {username}")
        return True

    def login(self, username: str, password: str) -> bool:
        if not username or not password:
            raise ValidationError("Username and password cannot be empty")
        if self.users.get(username) != password:
            logger.warning(f"Failed login attempt: {username}")
            raise InvalidCredentialsError("Invalid username or password")
        logger.info(f"Successful login: {username}")
        return True
