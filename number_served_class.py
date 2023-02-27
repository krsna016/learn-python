"""..."""


class NumberServed():
    """..."""

    def __init__(self):
        """..."""
        self.number_served = 0

    def set_number_served(self,enter):
        """..."""
        if enter > self.number_served:
            self.number_served = enter

    def increment_number_served(self,enter):
        """..."""
        if enter > 0:
            self.number_served += enter


restaurant = NumberServed()
print(f"Number served : {restaurant.number_served}")
served = int(input("The number of customer the restaurant served : "))
print(restaurant.set_number_served.__doc__)
restaurant.set_number_served(served)
print(f"Number served : {restaurant.number_served}")
served = int(input("The number of customer the restaurant served : "))
print(restaurant.increment_number_served.__doc__)
restaurant.increment_number_served(served)
print(f"Number served : {restaurant.number_served}")
