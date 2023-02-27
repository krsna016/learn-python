"""This is a admin class"""


from the_user_class import User


class Admin(User):
    """This is the admin class for showing the privileges"""

    def __init__(self, first_name, last_name, *args):
        """Initialising the attributes for the class"""
        super().__init__(first_name, last_name)
        self.arguments = args

    def show_privileges(self):
        """This method will show the privileges"""
        print("The privileges are : ")
        for i in self.arguments:
            print("-", i)


user_1 = Admin("Anurag", "Pareek", "can add post",
               "can delete post", "can ban user")
user_1.show_privileges()
user_1.describe_user()
