"""..."""


class User():
    """..."""

    def __init__(self,login_attempts):
        """..."""
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        """..."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """..."""
        self.login_attempts = 0


user_1 = User(10)
print("Login attempts = ",user_1.login_attempts)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("Login attempts = ",user_1.login_attempts)
user_1.reset_login_attempts()
print("Login attempts = ",user_1.login_attempts)
