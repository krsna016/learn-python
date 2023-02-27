# This is called the module docstring:
"""...Start creating a class..."""

class Restaurant():
    """...Creating a class of restaurant needs..."""

    def __init__(self,restaurant_name,cuisine_type):
        """...Initialising the attributes for the class..."""
        self.r_name = restaurant_name
        self.c_type = cuisine_type

    def describe_restaurant(self):
        """...Method to describe the restaurant..."""
        print(f"Our restaurant name is : {self.r_name}")
        print(f"The cuisine type is : {self.c_type}")

    def open_restaurant(self):
        """...Method to tell when the restaurant is open..."""
        print(f"The restaurant named {self.r_name} is open in all 7 days 24 hours")

# print(Restaurant.__doc__)
# the_restaurant = Restaurant("XYZ restaurant","Soft")
# the_another_restaurant = Restaurant("ABC restaurant","Tight")
# print(the_restaurant.describe_restaurant.__doc__)
# the_restaurant.describe_restaurant()
# print(the_restaurant.open_restaurant.__doc__)
# the_restaurant.open_restaurant()
# print()
# print(the_another_restaurant.describe_restaurant.__doc__)
# the_another_restaurant.describe_restaurant()
# print(the_another_restaurant.open_restaurant.__doc__)
# the_another_restaurant.open_restaurant()
