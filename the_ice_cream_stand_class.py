"""This will generate a data of flavours"""


from the_restaurant_class import Restaurant


class IceCreamStand(Restaurant):
    """Try to accomplish a flavour method inherits from restaurant class"""

    def __init__(self, restaurant_name, cuisine_type, *flavours):
        """Initialising the attributes for the class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def display_flavours(self):
        """This method will display the flavours"""
        print("The available flavours are : ")
        for i in self.flavours:
            print("-", i)


this_flavour = IceCreamStand("ABC", "SOFT", "VENILLA", "CHOCOLATE")
this_flavour.display_flavours()
