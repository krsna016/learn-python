# This is the doctring for the module:
""" ***** Start creating a class ***** """


# Here we are creating a class (not child class) telling about the environment inside
# the electric car and we use the instances of thee class as attributes in 
# the electriccar class and access it:
class Environment():
    # This are docstring:
    """ ***** Creating a method to describe the car's environment inside ***** """

    # Creating a method or attribute method:
    def __init__(self,ac_type = "First class AC",total_seats = 8):
        # This are docstring:
        """ ***** Initialising the attributes for the class ***** """
        self.ac_type = ac_type
        self.total_seats = total_seats

    # Creating a method or attribute method:
    def describe_ac(self):
        # This are docstring:
        """ ***** This will explain you about the type of 'AC' used in the car ***** """
        # Returning the message:
        return f"The ac used is : {self.ac_type}"
    
    def describe_seats(self):
        # This is the docstring:
        """ ***** This will explain you about the number of seats inside the car ***** """
        # Returning the message:
        return f"There are a total of {self.total_seats} seats in the car"

#-----------------------------Parent Class : Car()------------------------------

# This is the class defining the design of the car:
# This is the paren(super) class:
class Car():
    # This is the docstring for the class:
    """ ***** A simple attempt to design a car ***** """

    # This is the method or attribute method of the class:
    # We used __init__() method here (constructor) (which have self as argument)
    # which used to create instance for the class:
    def __init__(self, make, model, year):
        # This is the docstring for the method:
        """ ***** Initializing the attributes for the class ***** """
        # 'make','model' and 'year' are called the attributes of the class:
        self.make = make
        self.model = model
        self.year = year
        # Setting up this initial value, also now we not need to put the argument
        # for the same:
        self.odometer_reading = 0

    # This is method or attribute method of the class:
    def get_descriptive_name(self):
        # This is the docstring for the method:
        """ ***** Get the name of the car ***** """
        long_name = f"----> Name = {self.make}{self.model} {self.year}"
        # Returning the value of the method:
        # Instead, we can also print():
        return long_name

    # This is method or attribute method of the class:
    def read_odometer(self):
        # This is the docstring for the method:
        """ ***** Read the odometer reading ***** """
        # Returning the value of the method:
        # Instead, we can also print():
        return f"----> Odometer reading = {self.odometer_reading}"

    # This is method or attribute method of the class:
    def update_odometer(self,new_odometer_reading):
        # This is the docstring for the method:
        """ ***** Update the odometer reading ***** """
        # We input this condition so that now one tries to roll back the odometer
        # reading:
        if new_odometer_reading > self.odometer_reading:
            self.odometer_reading = new_odometer_reading
        else:
            return " ---- You can't roll back the odometer reading ---- "
        # Even if we don't write this the method will autometically return None:
        # Returning the value of the method:
        # Instead, we can also print():
        return None

    # This is method or attribute method of the class:
    def increment_odometer_reading(self,incremented_odometer_reading):
        # This is the docstring for the method:
        """ ***** Update the odometer reading ***** """
        # We input this condition so that now one tries to roll back the odometer
        # reading:
        if incremented_odometer_reading > 0:
            self.odometer_reading += incremented_odometer_reading
        else:
            print(" ---- You can't roll back the odometer reading ---- ")
        # Even if we don't write this the method will autometically return None:
        # Returning the value of the method:
        # Instead, we can also print():
        return None

    # This is method or attribute method of the class:
    def fill_gas_tank(self):
        # This is the doctring:
        """ ***** Checking whether the gas tank is filled ***** """
        # Returning the value:
        return "Yes, the gas tank is filled."

#-----------------------------Child Class : ElectricCar()-----------------------

# This is the child(sub) class:
class ElectricCar(Car):
    # This is the docstring:
    """
    ***** 
    This is the inheritance we create clild class of the parent class 'Car'
    This represent the aspect of the car, specific to 'Electric car'.
    ***** 
    """
    # We use the __init__() method to take the imformation required to create the
    # instance for the Car class:
    def __init__(self, make, model, year):
        # This is the docstring:
        """
        ***** 
        Initialising the attributes for the parent class 
        Then initialize attributes specific to an electric car
        *****
        """
        # The super() function at is a special function that helps Python make
        # connections between the parent and child class. This line tells Python to
        # call the __init__() method from ElectricCar’s parent class, which gives an
        # ElectricCar instance all the attributes of its parent class.
        super().__init__(make, model, year)
        # Defining attributes and methods for the child class:
        self.battery_size = 70
        self.car_environment = Environment()

    # This is method or attribute method of the class:
    def describe_battery(self):
        # This is the docstring:
        """ ***** Describing the battery of the electric car ***** """
        # Returning the value:
        return f"The car has {self.battery_size} Kwh battery."

    # This is method or attribute method of the class:
    def fill_gas_tank(self):
        # This is the docstring:
        """ ***** We have no need of gas tank here ***** """
        # Returning the value:
        return "We have no need of gas tank, here."

    # # This is method or attribute method of the class:
    # def change_battery(self,size):
    #     # This is docstring:
    #     """ ***** Changing the battery size ***** """
    #     self.battery_size = size
    #     # Even if we don't write this the method will autometically return None:
    #     # Returning the value of the method:
    #     # Instead, we can also print():
    #     return None




#----------------------------- For parent class --------------------------------

# # Creating the variable to store the instance:
# # This is also called the 'object' of the class:
# # This line calls the __init__() method defined in Car class and create the instance:
# car_1 = Car("Audi", "A2", "2023")
# # Printing the docstrings and the method and the attributes etc:
# print(car_1.get_descriptive_name.__doc__)
# car_1.get_descriptive_name()
# print()
# print(car_1.read_odometer.__doc__)
# print(car_1.read_odometer())
# print()

# # It's the (method 1) to change the odometer reading by directly accessing the
# # attribute:

# # update_reading = int(input("What's the latest reading in the odometer : "))
# # car_1.odometer_reading += update_reading
# # print("...Odometer reading updated...")
# # print(car_1.read_odometer.__doc__)
# # print(car_1.read_odometer())
# # print("...Odometer reading updated...\n")

# # It's the (method 2) to change the odometer reading using the method:

# update_reading = int(input("What's the latest odometer reading value : "))
# print(car_1.update_odometer.__doc__)
# car_1.update_odometer(update_reading)
# print(car_1.read_odometer.__doc__)
# print(car_1.read_odometer())
# print("...Odometer reading updated...\n")

# # It's the (method 3) to change the odometer reading by incrementing the odometer
# # reading through method:

# increment_reading = int(input("What's the latest odometer incremented reading : "))
# print(car_1.increment_odometer_reading.__doc__)
# car_1.increment_odometer_reading(increment_reading)
# print(car_1.read_odometer.__doc__)
# print(car_1.read_odometer())
# print("...Odometer reading updated...\n")

#------------------------------ For child class --------------------------------

# # Creating the variable to store the instance:
# # This is also called the 'object' of the class:
# # This line calls the __init__() method defined in ElectricCar,
# # which in turn tells Python to call the __init__() method defined in the parent
# # class Car.
# e_car_1 = ElectricCar("Tesla","3","2023")
# print(e_car_1.describe_battery.__doc__)
# print(e_car_1.describe_battery())
# print()
# print(e_car_1.fill_gas_tank.__doc__)
# print(e_car_1.fill_gas_tank())
# print()
# e_car_1.change_battery(980)
# print(e_car_1.describe_battery.__doc__)
# print(e_car_1.describe_battery())
# print()
# # Accessing the instances as attributes:
# print(e_car_1.car_environment.describe_seats.__doc__)
# print(e_car_1.car_environment.describe_seats())
# print()
# print(e_car_1.car_environment.describe_ac.__doc__)
# print(e_car_1.car_environment.describe_ac())
