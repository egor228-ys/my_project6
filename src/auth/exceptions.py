class AuthError(Exception):
    pass

class ValidationError(AuthError):
    pass

class UserExistsError(AuthError):
    pass

class InvalidCredentialsError(AuthError):
    pass
