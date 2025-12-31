class UserServiceError(Exception):
    """Base exception for all user service-related errors in MAS Eval."""


class EmailAlreadyRegisteredError(UserServiceError):
    """Raised when attempting to register with an email that already exists."""

    def __init__(self, email: str, message: str = "Email already registered"):
        self.email = email
        self.message = message
        super().__init__(f"{message}: {email}")


class UsernameAlreadyRegisteredError(UserServiceError):
    """Raised when attempting to register with a username that already exists."""

    def __init__(self, username: str, message: str = "Username already registered"):
        self.username = username
        self.message = message
        super().__init__(f"{message}: {username}")
