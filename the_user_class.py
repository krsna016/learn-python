"""Start creating the class"""


class User():
    """...Creating a user class to describe the user..."""

    def __init__(self, first_name, last_name):
        """...Initialising the attributes for the class..."""
        self.f_name = first_name
        self.l_name = last_name

    def describe_user(self):
        """...Describing the user..."""
        print(f"The name of the user is : {self.f_name} {self.l_name}")

    def greet_user(self):
        """...Greeting the user..."""
        print(f"Nice to meet you, {self.f_name} {self.l_name}")


# user_1 = User("Anurag", "Pareek")
# print(user_1.describe_user.__doc__)
# user_1.describe_user()
# print()
# print(user_1.greet_user.__doc__)
# user_1.greet_user()
